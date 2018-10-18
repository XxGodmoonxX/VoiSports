from tuning import Tuning
import usb.core
import usb.util
import time
import serial
# import pyaudio
# import time
# import numpy
#
# audioChank = 1024*8
# audioWidth = 2
# audioRate = 9600
# audioChn = 1
# input_device_index = 0
#
# p = pyaudio.PyAudio()
#
# stream = p.open( format = pyaudio.paInt16,\
# 			channels = audioChn,\
# 			rate = audioRate,\
# 			input_device_index = input_device_index,\
# 			input = True,\
# 			frames_per_buffer = audioChank )
dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)
ser = serial.Serial("/dev/cu.usbmodem14121", 10000, timeout=None)
if ser:
    Mic_tuning = Tuning(dev)
    while True:
        # data =  stream.read( audioChank )
        # a =  numpy.frombuffer( data, dtype = "int16" )
        # print a
        # if a.max() > 6000:
        if Mic_tuning.is_voice() == 1:
            print Mic_tuning.direction
            if(0 <= Mic_tuning.direction <= 5):
                flag = '3'
            if(5 < Mic_tuning.direction <= 10):
                flag = '2';
            if(10 < Mic_tuning.direction <= 15):
                flag = '1';
            if(15 < Mic_tuning.direction <= 20):
                flag = 'z';
            if(20 < Mic_tuning.direction <= 25):
                flag = 'y';
            if(25 < Mic_tuning.direction <= 30):
                flag = 'x';
            if(30 < Mic_tuning.direction <= 35):
                flag = 'w';
            if(35 < Mic_tuning.direction <= 40):
                flag = 'v';
            if(40 < Mic_tuning.direction <= 45):
                flag = 'u';
            if(45 < Mic_tuning.direction <= 50):
                flag = 't';
            if(50 < Mic_tuning.direction <= 55):
                flag = 's';
            if(55 < Mic_tuning.direction <= 60):
                flag = 'r';
            if(60 < Mic_tuning.direction <= 65):
                flag = 'q';
            if(65 < Mic_tuning.direction <= 70):
                flag = 'p';
            if(70 < Mic_tuning.direction <= 75):
                flag = 'o';
            if(75 < Mic_tuning.direction <= 80):
                flag = 'n';
            if(80 < Mic_tuning.direction <= 85):
                flag = 'm';
            if(85 < Mic_tuning.direction <= 90):
                flag = 'l';
            if(90 < Mic_tuning.direction <= 95):
                flag = 'k';
            if(95 < Mic_tuning.direction <= 100):
                flag = 'j';
            if(100 < Mic_tuning.direction <= 105):
                flag = 'i';
            if(105 < Mic_tuning.direction <= 110):
                flag = 'h';
            if(110 < Mic_tuning.direction <= 115):
                flag = 'g';
            if(115 < Mic_tuning.direction <= 120):
                flag = 'f';
            if(120 < Mic_tuning.direction <= 125):
                flag = 'e';
            if(125 < Mic_tuning.direction <= 130):
                flag = 'd';
            if(130 < Mic_tuning.direction <= 135):
                flag = 'c';
            if(135 < Mic_tuning.direction <= 140):
                flag = 'b';
            if(140 < Mic_tuning.direction <= 145):
                flag = 'a';
            if(145 < Mic_tuning.direction <= 150):
                flag = 'a';
            if(355 < Mic_tuning.direction <= 360):
                flag = '4';
            if(350 < Mic_tuning.direction <= 355):
                flag = '5';
            if(345 < Mic_tuning.direction <= 350):
                flag = '6';
            if(340 < Mic_tuning.direction <= 345):
                flag = '7';
            if(335 < Mic_tuning.direction <= 340):
                flag = '8';
            if(330 < Mic_tuning.direction <= 335):
                flag = '9';
            if(325 < Mic_tuning.direction <= 330):
                flag = '9';
            if(320 < Mic_tuning.direction <= 325):
                flag = '9';
            if(315 < Mic_tuning.direction <= 320):
                flag = '9';
            print flag
            ser.write(flag)
            time.sleep(0.1)
            if(flag == '@'):
                break;
            flag =';';
    # stream.close()
    # p.terminate()
    ser.close()
