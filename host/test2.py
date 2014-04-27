import imp
import time
import signal
import sys
import atexit

from random import randint

from tricolorLED import TricolorLED

def signal_handler(signal, frame):
        closeSerial()
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

def closeSerial():
    myLED.close()
atexit.register(closeSerial)

myLED = TricolorLED(9)
#myLED.connect(9)

rLast = 0
gLast = 0
bLast = 0

while 1:
    rNew = randint(0, 255)
    gNew = randint(0, 255)
    bNew = randint(0, 255)

    res = 100.0
    
    for step in range(int(res)):
        myLED.setColor(rLast + (rNew-rLast)*(step/res),
                     gLast + (gNew-gLast)*(step/res),
                     bLast + (bNew-bLast)*(step/res))
        time.sleep(0.01)
    
    rLast = rNew
    gLast = gNew
    bLast = bNew
