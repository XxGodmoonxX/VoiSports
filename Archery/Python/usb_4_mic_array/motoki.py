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

#for i in range( audioRate/audioChank * 60 ):
while True:
	data =  stream.read( audioChank )
	a =  numpy.frombuffer( data, dtype = "int16" ) #convert int
	print a.max()

stream.close()
p.terminate()