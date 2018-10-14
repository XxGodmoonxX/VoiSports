from tuning import Tuning
import usb.core
import usb.util
import time
import serial

dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)
ser = serial.Serial("/dev/cu.usbmodem14221", 9600, timeout=None)
if ser:
    Mic_tuning = Tuning(dev)
    while True:
        # if Mic_tuning.is_voice() == 1:
            print Mic_tuning.direction
            if(0 <= Mic_tuning.direction <= 5):
                flag = 'a'
            if(5 < Mic_tuning.direction <= 10):
                flag = 'b';
            if(10 < Mic_tuning.direction <= 15):
                flag = 'c';
            if(15 < Mic_tuning.direction <= 20):
                flag = 'd';
            if(20 < Mic_tuning.direction <= 25):
                flag = 'e';
            if(25 < Mic_tuning.direction <= 30):
                flag = 'f';
            if(30 < Mic_tuning.direction <= 35):
                flag = 'g';
            if(35 < Mic_tuning.direction <= 40):
                flag = 'h';
            if(40 < Mic_tuning.direction <= 45):
                flag = 'i';
            if(45 < Mic_tuning.direction <= 50):
                flag = 'j';
            if(50 < Mic_tuning.direction <= 55):
                flag = 'k';
            if(55 < Mic_tuning.direction <= 60):
                flag = 'l';
            if(60 < Mic_tuning.direction <= 65):
                flag = 'm';
            if(65 < Mic_tuning.direction <= 70):
                flag = 'n';
            if(70 < Mic_tuning.direction <= 75):
                flag = 'o';
            if(75 < Mic_tuning.direction <= 80):
                flag = 'p';
            if(80 < Mic_tuning.direction <= 85):
                flag = 'q';
            if(85 < Mic_tuning.direction <= 90):
                flag = 'r';
            if(90 < Mic_tuning.direction <= 95):
                flag = 's';
            if(95 < Mic_tuning.direction <= 100):
                flag = 't';
            if(100 < Mic_tuning.direction <= 105):
                flag = 'u';
            if(105 < Mic_tuning.direction <= 110):
                flag = 'v';
            if(110 < Mic_tuning.direction <= 115):
                flag = 'w';
            if(115 < Mic_tuning.direction <= 120):
                flag = 'x';
            if(120 < Mic_tuning.direction <= 125):
                flag = 'y';
            if(125 < Mic_tuning.direction <= 130):
                flag = 'z';
            if(130 < Mic_tuning.direction <= 135):
                flag = '0';
            if(135 < Mic_tuning.direction <= 140):
                flag = '1';
            if(140 < Mic_tuning.direction <= 145):
                flag = '2';
            if(145 < Mic_tuning.direction <= 150):
                flag = '3';
            if(150 < Mic_tuning.direction <= 155):
                flag = '4';
            if(155 < Mic_tuning.direction <= 160):
                flag = '5';
            if(160 < Mic_tuning.direction <= 165):
                flag = '6';
            if(165 < Mic_tuning.direction <= 170):
                flag = '7';
            if(170 < Mic_tuning.direction <= 175):
                flag = '8';
            if(175 < Mic_tuning.direction <= 180):
                flag = '9';
            if(180 < Mic_tuning.direction <= 270):
                flag = flag;
            print flag
            ser.write(flag)
            time.sleep(0.1)
            if(flag == '@'):
                break;
    ser.close()
