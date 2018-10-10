from tuning import Tuning
import usb.core
import usb.util
import time
import serial

dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)
ser = serial.Serial("/dev/cu.wchusbserial1420", 9600, timeout=None)
if ser:
    Mic_tuning = Tuning(dev)
    while True:
        print Mic_tuning.direction
        if(0 <= Mic_tuning.direction <= 180):
            flag = 'a'
        if(180 < Mic_tuning.direction <= 360):
            flag = 'b';
        print flag
        ser.write(flag)
        time.sleep(1)
        if(flag == '@'):
            break;
    ser.close()
