
import serial
ser=serial.Serial('/dev/ttyACM2', 9600)

while(1):
	freq = ser.read()
	#freq1 = "0"
	#print freq
	#while (freq!="E"):
	 # 	freq1 += freq
	#	freq1 = freq1*10
	#	print freq1
	try:
		c = int(freq)
	except ValueError:
		pass
	finally:
		print c

		from ctypes import *
		from contextlib import contextmanager
		import pyaudio
		import math
		import numpy as np

		ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)

		def py_error_handler(filename, line, function, err, fmt):
		    pass

		c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

		@contextmanager
		def noalsaerr():
		    asound = cdll.LoadLibrary('libasound.so')
		    asound.snd_lib_error_set_handler(c_error_handler)
		    yield
		    asound.snd_lib_error_set_handler(None)

		with noalsaerr():
			#sudo apt-get install python-pyaudio
			PyAudio = pyaudio.PyAudio

			#See http://en.wikipedia.org/wiki/Bit_rate#Audio
			BITRATE = 16000 #number of frames per second/frameset.      

			#See http://www.phy.mtu.edu/~suits/notefreqs.html
			FREQUENCY = c*200 #Hz, waves per second, 261.63=C4-note.
			LENGTH = 0.200 #seconds to play sound

			NUMBEROFFRAMES = int(BITRATE * LENGTH)
			RESTFRAMES = NUMBEROFFRAMES % BITRATE
			WAVEDATA = ''    

			for x in xrange(NUMBEROFFRAMES):
			 WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))    

			#fill remainder of frameset with silence
			for x in xrange(RESTFRAMES): 
			 WAVEDATA = WAVEDATA+chr(128)

			p = PyAudio()
			stream = p.open(format = p.get_format_from_width(1), 
			                channels = 1, 
			                rate = BITRATE, 
			                output = True)
			stream.write(WAVEDATA)
			stream.stop_stream()
			stream.close()
			p.terminate()

			
