import wave,pyaudio,sys


class playfile():
	# open the file for reading.
		def play(self,filename):
			wf = wave.open(filename, 'rb')
			chunk=wf.getnframes()

			# create an audio object
			p = pyaudio.PyAudio()

			# open stream based on the wave object which has been input.
			stream = p.open(format =
                		p.get_format_from_width(wf.getsampwidth()),
                		channels = wf.getnchannels(),
                		rate = wf.getframerate(),
                		output = True)

			# read data (based on the chunk size)
			data = wf.readframes(chunk)

			# play stream (looping from beginning of file to the end)
			while data != '':
    				# writing to the stream is what *actually* plays the sound.
    				stream.write(data)
    				data = wf.readframes(chunk)

			# cleanup stuff.
			stream.close()    
			p.terminate()


#a=playfile()
#a.play("mario.wav")
