import os,gtk,sys,signal,gobject,time
from p1 import dsaa
from play import playfile
from record import record


class Wave(gtk.Window):
    def get_resource_path(self,rel_path):
	 dir_of_py_file = os.path.dirname(__file__)
	 rel_path_to_resource = os.path.join(dir_of_py_file, rel_path)
	 abs_path_to_resource = os.path.abspath(rel_path_to_resource)
	 return abs_path_to_resource





    def on_mix_modulate(self,widget,val):
	 #mixing
	 l1=list()
	 l2=list()
	 if(val==0):
	      for i in range(3):
		   if(self.mixing[i]==True):
			l.append(self.song[i])
	      self.waveobject[val].Modulate(l,"temp3.wav")
	      pid1=os.fork()
	      if(pid1==0):
	      	a=playfile()
	      	a.play("temp3.wav")
	 else:
	      for i in range(3):
		   if(self.modulation[i]==True):
			l1.append(self.song[i])
			if(self.reversal[i]==True):
			     l2.append(True)
			else:
			     l2.append(False)
			if(self.scale[i]>1):
			     l2.append(self.scale[i])
			else:
			     l2.append(1)
			if(self.shift[i]!=0):
			     l2.append(self.shift[i])
			else:
			     l2.append(0)
	      self.waveobject[val].Modulate(l1,"temp4.wav",l2)
	      pid2=os.fork()
	      if(pid2==0):
		   a=playfile()
		   a.play("temp4.wav")
	      



    def on_click_play_button(self,widget,val):
	 if(self.pid1[val]>0):
	      os.kill(self.pid1[val],9)
	      self.pid1[val]=-1
	      self.elapsed[val]=0
	      self.runtime[val] = time.time()
	      self.played[val]=False
	 else:
	      self.progressbar[val].set_fraction(0.0)
	      print self.pid1
	      pid=os.fork() 
	      self.pid1[val]=pid
	      self.played[val]=True
	      if(val<=2):
		   print self.waveobject[0].parameters
		   print "amplitude " ,self.amp[val]
	           self.waveobject[val].Amplify(self.song[val],self.amp[val],"temp"+str(val)+".wav")
		   if(self.reversal[val]==True):
				self.waveobject[val].Reverse("temp"+str(val)+".wav","temp"+str(val)+".wav")
		   if(self.scale[val]>1):
	                	self.waveobject[val].Scale("temp"+str(val)+".wav",self.scale[val],"temp"+str(val)+".wav")
	           if(self.shift[val]!=0):
				self.waveobject[val].Shift("temp"+str(val)+".wav",self.shift[val],"temp"+str(val)+".wav")
		   self.waveobject[val].WriteFile("temp"+str(val)+".wav",self.waveobject[val].parameters,self.waveobject[val].data)
		   print self.waveobject[0].parameters
	      else:
		   if(val==4):
			l=[]
			for i in range(3):
			     if(self.modulation[i]==True):
				  self.waveobject[val].Amplify(self.song[i],self.amp[i],"temp"+str(i)+".wav")
		   		  if(self.reversal[i]==True):
					self.waveobject[i].Reverse("temp"+str(i)+".wav","temp"+str(i)+".wav")
		   		  if(self.scale[i]>1):
	                		self.waveobject[i].Scale("temp"+str(i)+".wav",self.scale[i],"temp"+str(i)+".wav")
	           		  if(self.shift[i]!=0):
					self.waveobject[i].Shift("temp"+str(i)+".wav",self.shift[i],"temp"+str(i)+".wav")
		   		  self.waveobject[i].WriteFile("temp"+str(i)+".wav",self.waveobject[i].parameters,self.waveobject[i].data)
				  l.append("temp"+str(i)+".wav")
			     print l
			     self.waveobject[val].Modulate(l,"temp4.wav")
	           elif(val==3):
			l=[]
		   	for i in range(3):
				if(self.mixing[i]==True):
			     		self.waveobject[i].Amplify(self.song[i],self.amp[i],"temp"+str(i)+".wav")
			     		if(self.reversal[i]==True):
				  		self.waveobject[i].Reverse("temp"+str(i)+".wav","temp"+str(i)+".wav")
		   	     		if(self.scale[i]>1):
	                     	  		self.waveobject[i].Scale("temp"+str(i)+".wav",self.scale[i],"temp"+str(i)+".wav")
	           	     		if(self.shift[i]!=0):
			     	  		self.waveobject[i].Shift("temp"+str(i)+".wav",self.shift[i],"temp"+str(i)+".wav")
		   	     		self.waveobject[i].WriteFile("temp"+str(i)+".wav",self.waveobject[i].parameters,self.waveobject[i].data)
			     		l.append("temp"+str(i)+".wav")
				print l
			self.waveobject[val].Mix(l,"temp3.wav")
	      self.elapsed[val] = 0.0
	      self.runtime[val]=time.time()
	      if(pid==0):
		   	a=playfile()
		   	print self.played[val]
	 	   	a.play("temp"+str(val)+".wav")
		   	sys.exit(0)



    def on_click_pause_button(self,widget,val):
	 if(self.pause[val]==False):
	      os.kill(self.pid1[val],signal.SIGSTOP)
	      self.elapsed[val]= self.elapsed[val]+time.time()-self.runtime[val]
	      self.runtime[val] = 0.0
	      self.pause[val]=True
	 else:
	      os.kill(self.pid1[val],signal.SIGCONT)
	      self.runtime[val] = time.time()
	      self.pause[val] = False







    def callbackreversal(self, widget, val):
	 print self.waveobject[0].parameters
	 if(self.reversal[val]==False):
	      self.reversal[val]=True
	 else:
	      self.reversal[val]=False
	 print "%s was toggled %s" % (val, widget.get_active())
	

    def callbackmodulation(self, widget, val):
	 if(self.modulation[val]==False):
	      self.modulation[val]=True
	 else:
	      self.modulation[val]=False
	 print "%s was toggled %s" % (val,widget.get_active())

    def callbackmixing(self, widget, val):
	 if(self.mixing[val]==False):
	      self.mixing[val]=True
	 else:
	      self.mixing[val]=False
	 print "%s was toggled %s" % (val,widget.get_active())
    
    
    def progress_timeout(self,pbobj):
	 for i in range(5):
	        if(self.pid1[i]>=0):
		     # print self.waveobject[i].parameters
		     self.progressbar[i].set_fraction(((self.elapsed[i]+time.time()-self.runtime[i])/(self.waveobject[i].parameters[3]/self.waveobject[i].parameters[2])))
	 return True
    
    
    def __init__(self):
	 super(Wave,self).__init__()
	 self.set_title("DSAA")
	 self.set_size_request(700,600)
	 self.set_position(gtk.WIN_POS_CENTER)
	 try:
	 	img=gtk.Image()
	 	self.set_icon_from_file(self.get_resource_path("icon.jpg"))
	 except:
	      pass


	 #progress bar
	 self.timer = gobject.timeout_add (100, self.progress_timeout, self)

	 button1=gtk.Button("Choose File")
	 button1.connect("clicked", self.on_file_clicked,0)
	 button2=gtk.Button("Choose File")
	 button2.connect("clicked", self.on_file_clicked,1)
	 button3=gtk.Button("Choose File")
	 button3.connect("clicked", self.on_file_clicked,2)
	 self.fixed=gtk.Fixed()
	 self.add(self.fixed)
	 self.fixed.show()
	 self.fixed.put(button1, 10, 30)
	 self.fixed.put(button2, 220, 30)
	 self.fixed.put(button3, 430, 30)
	 self.label=list()
	 for i in range(3):
	      self.label.append(gtk.Label("No File Selected"))
	 self.fixed.put(self.label[0],100,35)
	 self.fixed.put(self.label[1],310,35)
	 self.fixed.put(self.label[2],520,35)


	 #make dsaa objects


	 #make objects of dssa
	 self.waveobject=list()
	 for i in range(5):
	      self.waveobject.append(dsaa())

	 #make recording object
	 self.rec = record()
	 self.rec.stop = False

	 self.is_recording = False

	 #pause
	 self.pause = list()
	 for i in range(5):
	      self.pause.append(False)

	 #which songs are played
	 self.played=list()
	 for i in range(5):
	      self.played.append(True)

	 #select song
	 self.song=list()
	 for i in range(3):
	      self.song.append(None)


	 self.elapsed=list()
	 for i in range(5):
	      self.elapsed.append(0)
	 self.runtime=list()
	 for i in range(5):
	      self.runtime.append(0)


	 #pids of the processes if(-1) no song is being played
	 self.pid1=list()
	 for i in range(5):
	     self.pid1.append(-1)

	 #set the amplitudes
	 self.amp=list()
	 for i in range(3):
	      self.amp.append(1)

	 #set time reversal
	 self.reversal=list()
	 for i in range(3):
	      self.reversal.append(False)



	 #set modulation
	 self.modulation=list()
	 for i in range(3):
	      self.modulation.append(False)



	 #set mixing
	 self.mixing = list()
	 for i in range(3):
	      self.mixing.append(False)


	 #Time shift
	 self.shift = list()
	 for i in range(3):
	      self.shift.append(0)



	 #Time Scale
	 self.scale = list()
	 self.timescale = list()
	 for i in range(3):
	      self.scale.append(0)



	 #Time Reversal
	 self.checkreversal=list()
	 for i in range(3):
	      button = gtk.CheckButton("Time Reversal",False)
	      button.connect("toggled", self.callbackreversal,i)
	      self.checkreversal.append(button)
	 self.fixed.put(self.checkreversal[0],30,300)
	 self.fixed.put(self.checkreversal[1],240,300)
	 self.fixed.put(self.checkreversal[2],450,300)


	 #Select For Modulation
	 self.checkmodulation=list()
	 for i in range(3):
	      button = gtk.CheckButton("Select For Modulation",False)
	      button.connect("toggled", self.callbackmodulation,i)
	      self.checkmodulation.append(button)
	 self.fixed.put(self.checkmodulation[0],30,350)
	 self.fixed.put(self.checkmodulation[1],240,350)
	 self.fixed.put(self.checkmodulation[2],450,350)



	 #Select For Mixing
	 self.checkmixing=list()
	 for i in range(3):
	      button = gtk.CheckButton("Select For Mixing",False)
	      button.connect("toggled", self.callbackmixing,i)
	      self.checkmixing.append(button)
	 self.fixed.put(self.checkmixing[0],30,400)
	 self.fixed.put(self.checkmixing[1],240,400)
	 self.fixed.put(self.checkmixing[2],450,400)


	 #Amplitude Scaling
	 self.fixed.put(gtk.Label("Amplitude"),30 ,85)
	 self.fixed.put(gtk.Label("Amplitude"),240 ,85)
	 self.fixed.put(gtk.Label("Amplitude"),450 ,85)
	 self.amplitude=list()
	 for i in range(3):
	 	scale=gtk.HScale()
	 	scale.set_range(1,5)
	 	scale.set_increments(0.5, 1)
	 	scale.set_digits(1)
	 	scale.set_size_request(160, 45)
	 	scale.connect("value-changed", self.amplitude_on_scale_change,i)
	 	self.amplitude.append(scale)
	 self.fixed.put(self.amplitude[0],30,100)
	 self.fixed.put(self.amplitude[1],240,100)
	 self.fixed.put(self.amplitude[2],450,100)


	 #Time Shift
	 self.fixed.put(gtk.Label("Time Shift"),30 ,160)
	 self.fixed.put(gtk.Label("Time Shift"),240 ,160)
	 self.fixed.put(gtk.Label("Time Shift"),450 ,160)
	 self.timeshift=list()
	 for i in range(3):
	 	scale=gtk.HScale()
	 	scale.set_range(-10,10)
	 	scale.set_increments(0.5, 1)
	 	scale.set_digits(1)
	 	scale.set_size_request(160, 45)
	 	scale.connect("value-changed", self.shift_on_scale_change,i)
	 	self.timeshift.append(scale)
	 self.fixed.put(self.timeshift[0],30,175)
	 self.fixed.put(self.timeshift[1],240,175)
	 self.fixed.put(self.timeshift[2],450,175)


   
	 #Time Scaling
	 self.fixed.put(gtk.Label("Time Scaling"),30 ,235)
	 self.fixed.put(gtk.Label("Time Scaling"),240 ,235)
	 self.fixed.put(gtk.Label("Time Scaling"),450 ,235)
	 self.timescale=list()
	 for i in range(3):
	 	scale=gtk.HScale()
	 	scale.set_range(0,30)
	 	scale.set_increments(0.5, 1)
	 	scale.set_digits(1)
	 	scale.set_size_request(160, 45)
	 	scale.connect("value-changed", self.scale_on_scale_change,i)
	 	self.timescale.append(scale)
	 self.fixed.put(self.timescale[0],30,250)
	 self.fixed.put(self.timescale[1],240,250)
	 self.fixed.put(self.timescale[2],450,250)

	 #Play Button
	 playbutton=list()
	 for i in range(3):
	      button=gtk.Button("Play/Stop")
	      button.connect("clicked", self.on_click_play_button,i)
	      playbutton.append(button)
	 self.fixed.put(playbutton[0],30,450)
	 self.fixed.put(playbutton[1],240,450)
	 self.fixed.put(playbutton[2],450,450)


	 #Pause Button
	 pausebutton=list()
	 for i in range(3):
	      button=gtk.Button("Pause")
	      button.connect("clicked", self.on_click_pause_button,i)
	      pausebutton.append(button)
	 self.fixed.put(pausebutton[0],110,450)
	 self.fixed.put(pausebutton[1],320,450)
	 self.fixed.put(pausebutton[2],530,450)
	 
	 
	 
	 #Mix Button
	 mixbutton = gtk.Button("Mix and Play")
	 mixbutton.connect("clicked",self.on_click_play_button,3)
	 self.fixed.put(mixbutton,50,530)


	 #Modulate Button
	 modbutton = gtk.Button("Modulate and Play")
	 modbutton.connect("clicked",self.on_click_play_button,4)
	 self.fixed.put(modbutton,250,530)


	 #Record Button
	 recordbutton = gtk.Button("Start/Stop Recording")
	 recordbutton.connect("clicked",self.on_click_record_button)
	 self.fixed.put(recordbutton,450,530)


	 #Progress Bar for Mix
#	 progressmix = gtk.ProgressBar(None)
#	 progressmix.set_orientation(gtk.PROGRESS_LEFT_TO_RIGHT)
#	 self.fixed.put(progressmix,110,570)


	 #Progress Bar for Modulate
#	 progressmodulate = gtk.ProgressBar(None)
#	 progressmodulate.set_orientation(gtk.PROGRESS_LEFT_TO_RIGHT)
#	 self.fixed.put(progressmodulate,330,570)
	 
	 
	 #Progress Bar
	 self.progressbar=list()
	 for i in range(5):
	      progress = gtk.ProgressBar(None)
	      progress.set_orientation(gtk.PROGRESS_LEFT_TO_RIGHT)
	      progress.set_fraction(0.0)
	      self.progressbar.append(progress)
         self.fixed.put(self.progressbar[0],30,500)
         self.fixed.put(self.progressbar[1],240,500)
         self.fixed.put(self.progressbar[2],450,500)
         self.fixed.put(self.progressbar[3],20,570)
         self.fixed.put(self.progressbar[4],240,570)



 	
    def on_click_record_button(self,widget):
	 if(self.is_recording==False):
	        pid = os.fork()
		self.is_recording = True
		if(pid==0):
		     self.rec.record_to_file('demo.wav')
		     sys.exit(0)
	 else:
	        self.rec.stop = False
		self.is_recording = False
	 return



    def amplitude_on_scale_change(self,widget,val):
	 amount = self.amplitude[val].get_value()
	 print amount
	 self.amp[val]=amount
	# self.waveobject[val].Amplify(self.song[val],amount,self.song[val])
	 

    def shift_on_scale_change(self,widget,val):
	 amount = self.timeshift[val].get_value()
	 self.shift[val] = amount
	 


    def scale_on_scale_change(self,widget,val):
	 amount = self.timescale[val].get_value()
	 self.scale[val] = amount
	  

    def add_filters(self, dialog):
	   filter_any = gtk.FileFilter()
	   filter_any.add_pattern("*.wav")
	   filter_any.add_pattern("*.WAV")
	   dialog.add_filter(filter_any)
    
    def on_file_clicked(self,widget,val):
	 print val
	 dialog = gtk.FileChooserDialog(title="Select File",action=gtk.FILE_CHOOSER_ACTION_OPEN,
		                                      buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN,gtk.RESPONSE_OK))
	 self.add_filters(dialog)

     	 response = dialog.run()
     
     	 if response == gtk.RESPONSE_OK:
	         filename=dialog.get_filenames()[0].split('/')[-1]
		 self.label[val].set_label(filename)
		 self.song[val]=dialog.get_filenames()[0]
		 print filename
	#	 self.fixed.put(filename,50,30)
         	 print("Open clicked")
           	 print("File selected: " + dialog.get_filename())
     	 elif response == gtk.RESPONSE_CANCEL:
            	 print("Cancel clicked")

     	 dialog.destroy()

win = Wave()
win.connect("delete-event", gtk.main_quit)
win.show_all()
gtk.main()
