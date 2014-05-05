from tornado.web import RequestHandler, Application, StaticFileHandler
from tornado.ioloop import IOLoop
from os.path import join, dirname, abspath
from threading import Thread
from multiprocessing import Manager
from time import sleep
import json


LED_device = '/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_A900cfK3-if00-port0'
Thread.daemon = True
base = join(dirname(abspath(__file__)), 'assets')
manager = Manager()
led_queue = manager.Queue()


def run(queue):
    from tricolorLED import TricolorLED

    LED = TricolorLED(LED_device)

    while 1:
        data = queue.get()
        print(data)
        if len(data) == 2:
            if data[0] == u'set':
                LED.setColor(*data[1])
            elif data[0] == u'sleep':
                sleep(data[1])
            elif data[0] == u'stop' and data[1] is True:
                LED.setColor(0, 0, 0)


def clear_queue():
    while not led_queue.empty():
        led_queue.get()


class Index(RequestHandler):
    def get(self):
        self.write(open(join(base, 'html', 'index.html')).read())


class LEDController(RequestHandler):
    def post(self):
        red = self.get_argument('red', 0)
        green = self.get_argument('green', 0)
        blue = self.get_argument('blue', 0)
        clear_queue()
        led_queue.put([u'set', [red, green, blue]])


class LEDJobUploader(RequestHandler):
    def post(self):
        payload = self.get_argument('payload', None)
        clear = self.get_argument('clear', True)

        if payload:
            data = json.loads(payload)
            job = data['job']

            if clear:
                clear_queue()

            for item in job:
                led_queue.put(item)


def start(handlers):
    port = 8080
    application = Application(handlers)
    application.listen(port)
    print('Running on {}'.format(port))
    IOLoop.instance().start()


handlers = [
    (r'/', Index),
    (r'/set_color', LEDController),
    (r'/set_job', LEDJobUploader),
    (r'/static/(.*)', StaticFileHandler, {'path': base}),
]


if __name__ == '__main__':
    Thread(target=run, args=(led_queue,)).start()
    web_thread = Thread(target=start, args=(handlers,))
    web_thread.daemon = False
    web_thread.start()
