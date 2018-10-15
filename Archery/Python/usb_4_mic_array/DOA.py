from tuning import Tuning
import usb.core
import usb.util
import time
import serial
import pyaudio
import time
import numpy

audioChank = 1024
audioWidth = 2
audioRate = 44100
audioChn = 1
input_device_index = 0

p = pyaudio.PyAudio()

stream = p.open( format = pyaudio.paInt16,\
			channels = audioChn,\
			rate = audioRate,\
			input_device_index = input_device_index,\
			input = True,\
			frames_per_buffer = audioChank )
data =  stream.read( audioChank )
a =  numpy.frombuffer( data, dtype = "int16" )
dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)
ser = serial.Serial("/dev/cu.usbmodem1421", 9600, timeout=None)
if ser:
    Mic_tuning = Tuning(dev)
    while True:
        if a.max() > 4000:
            print Mic_tuning.direction
            if(0 <= Mic_tuning.direction <= 5):
                flag = '9'
            if(5 < Mic_tuning.direction <= 10):
                flag = '8';
            if(10 < Mic_tuning.direction <= 15):
                flag = '7';
            if(15 < Mic_tuning.direction <= 20):
                flag = '6';
            if(20 < Mic_tuning.direction <= 25):
                flag = '5';
            if(25 < Mic_tuning.direction <= 30):
                flag = '4';
            if(30 < Mic_tuning.direction <= 35):
                flag = '3';
            if(35 < Mic_tuning.direction <= 40):
                flag = '2';
            if(40 < Mic_tuning.direction <= 45):
                flag = '1';
            if(45 < Mic_tuning.direction <= 50):
                flag = '0';
            if(50 < Mic_tuning.direction <= 55):
                flag = 'z';
            if(55 < Mic_tuning.direction <= 60):
                flag = 'y';
            if(60 < Mic_tuning.direction <= 65):
                flag = 'x';
            if(65 < Mic_tuning.direction <= 70):
                flag = 'w';
            if(70 < Mic_tuning.direction <= 75):
                flag = 'v';
            if(75 < Mic_tuning.direction <= 80):
                flag = 'u';
            if(80 < Mic_tuning.direction <= 85):
                flag = 't';
            if(85 < Mic_tuning.direction <= 90):
                flag = 's';
            if(90 < Mic_tuning.direction <= 95):
                flag = 'r';
            if(95 < Mic_tuning.direction <= 100):
                flag = 'q';
            if(100 < Mic_tuning.direction <= 105):
                flag = 'p';
            if(105 < Mic_tuning.direction <= 110):
                flag = 'o';
            if(110 < Mic_tuning.direction <= 115):
                flag = 'n';
            if(115 < Mic_tuning.direction <= 120):
                flag = 'm';
            if(120 < Mic_tuning.direction <= 125):
                flag = 'l';
            if(125 < Mic_tuning.direction <= 130):
                flag = 'k';
            if(130 < Mic_tuning.direction <= 135):
                flag = 'j';
            if(135 < Mic_tuning.direction <= 140):
                flag = 'i';
            if(140 < Mic_tuning.direction <= 145):
                flag = 'h';
            if(145 < Mic_tuning.direction <= 150):
                flag = 'g';
            if(150 < Mic_tuning.direction <= 155):
                flag = 'f';
            if(155 < Mic_tuning.direction <= 160):
                flag = 'e';
            if(160 < Mic_tuning.direction <= 165):
                flag = 'd';
            if(165 < Mic_tuning.direction <= 170):
                flag = 'c';
            if(170 < Mic_tuning.direction <= 175):
                flag = 'b';
            if(175 < Mic_tuning.direction <= 180):
                flag = 'a';
            if(180 < Mic_tuning.direction <= 360):
                flag = '/';
            print flag
            ser.write(flag)
            time.sleep(0.1)
            if(flag == '@'):
                break;
            flag =';';
        a.zeros(0);
    ser.close()
