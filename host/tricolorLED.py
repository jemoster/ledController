import serial
import time

class TricolorLED:
    """An interface for controlling a Tricolor LED over the serial port"""
    
    ser = serial.Serial()
    def __init__(self,port):
        self.connect(port)
    
    def connect(self, port):
        self.close()
        self.ser = serial.Serial(port-1)
        self.ser.baudrate = 57600
        time.sleep(1)
    
    def setColor(self, red_t, green_t, blue_t):
        self.ser.write("S"+str(int(red_t))+","+str(int(green_t))+","+str(int(blue_t))+'\n')
    
    def close(self):
        self.ser.close()
        return not(self.ser.isOpen())
