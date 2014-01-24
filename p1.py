import wave, struct
class dsaa():
     	
        def __init__(self):
	     self.data=[]
	     self.parameters=tuple()
	     self.length=0
	     self.var=''

     	def ReadFile(self,SourceFile):
     		SourceWaveFile = wave.open(SourceFile,'r')
     		self.parameters = SourceWaveFile.getparams()
     		self.length = SourceWaveFile.getnframes()
     		waveData = SourceWaveFile.readframes(self.length)
	#	self.frames=[]
	#	for i in range(self.length):
	 # 		self.frames.append(SourceWaveFile.readframes(1))
		SourceWaveFile.close()
	#	if(parameters[1]==2):
		var = '%ih' %(self.parameters[0]*self.parameters[3])
	#	else:
	#	     var = '%iB' %(parameters[0]*parameters[3])
    		self.data = struct.unpack(var, waveData)
        
	def WriteFile(self,NewFile,parameters,data):
     		DestinationWaveFile = wave.open(NewFile,'w')
     		DestinationWaveFile.setparams(parameters)
	#	if(parameters[1]==2):
		var = '%ih' %(parameters[0]*parameters[3])
	#	else:
	#	     var = '%iB' %(parameters[0]*parameters[3])
     		newFile=struct.pack(var,*data)
     		DestinationWaveFile.writeframes(newFile)
     		DestinationWaveFile.close()



	def OpenSourceFile(self,FileName):
     		WaveFile = wave.open(FileName,'r')
     		return WaveFile

	def OpenDestinationFile(self,Filename):
     		WaveFile = wave.open(Filename,'w')
     		return WaveFile

	def Amplify(self,SourceFile,amount,NewFile):
	     #		SourceWaveFile = wave.open(SourceFile,'r')
	#	parameters = SourceWaveFile.getparams()
	#	length = SourceWaveFile.getnframes()
	#	waveData = SourceWaveFile.readframes(length)
	#	SourceWaveFile.close()
	#	DestinationWaveFile = wave.open(NewFile,'w')
	#	DestinationWaveFile.setparams(parameters)
	#	if(parameters[1]==2):
	#	var = '%ih' %(parameters[0]*parameters[3])
	#	else:
	#	     var = '%iB' %(parameters[0]*parameters[3])
    #		data = struct.unpack(var, waveData)
    		self.ReadFile(SourceFile)
     		l=[]
	#	for i in range(len(self.data)):
	 # 		l.append(self.data[i])
	 	self.data=list(self.data)
     		for i in range(len(self.data)):
	  		if(not((amount*(int(self.data[i])))<=32767 and (amount*(int(self.data[i])))>=-32767)):
	       			if((amount*(int(self.data[i])))<0):
		    			self.data[i]=-32767
	       			else:
		    			self.data[i]=32767
          		else:
	       			self.data[i]*=amount
		self.data=tuple(self.data)
	#        self.WriteFile(NewFile,self.parameters,self.data)
	#	newFile=struct.pack(var,*l)
	#	DestinationWaveFile.writeframes(newFile)
	#	DestinationWaveFile.close()

	def Reverse(self,SourceFile,DestinationFile):
	        if(self.parameters[0]==1):
	     		self.data=list(self.data)
	        	self.data.reverse()
			self.data=tuple(self.data)
	     #	SourceWaveFile = self.OpenSourceFile(SourceFile)
	#	parameters = SourceWaveFile.getparams()
	#	length = SourceWaveFile.getnframes()
#		print parameters
		else:
			SourceLeft=[]
			SourceRight=[]
			for i in range(0,len(self.data),2):
			     SourceLeft.append(self.data[i])
			     SourceRight.append(self.data[i+1])
			SourceLeft.reverse()
			SourceRight.reverse()
			l=[]
			for i in range(len(SourceLeft)):
			     l.append(SourceLeft[i])
			     l.append(SourceRight[i])
			self.data = tuple(l)
#		for i in range(length):
#	  		SourceLeft.append(SourceWaveFile.readframes(1))
#		SourceWaveFile.close()
#		DestinationWaveFile = self.OpenDestinationFile(DestinationFile)
#		DestinationWaveFile.setparams(parameters)
 #    		for i in reversed(SourceLeft):
#	  		DestinationWaveFile.writeframes(i)
#		DestinationWaveFile.close()

		#     for i in range(0,length):
		#	  if(i%2==0):
		#	       SourceLeft.append(SourceWaveFile.readframes(1))
		#	  else:
		#	       SourceRight.append(SourceWaveFile.readframes(1))
		 #    SourceRight.reverse()
		#     SourceLeft.reverse()
		 #    odd=even=0
		  #   print length
		   #  print len(SourceLeft)
		    # print len(SourceRight)
		#     for i in range(length):
		#	  if(i%2==0):
		#	       DestinationWaveFile.writeframes(SourceLeft[odd])
		#	       odd+=1
		#	  else:
		#	       DestinationWaveFile.writeframes(SourceRight[even])
		#	       even+=1


	def Scale(self,SourceFile,amount,NewFile):
	     	


		count = 0
		new = list()
	        self.data=list(self.data)
		data = self.data
		self.parameters = list(self.parameters)
		if(self.parameters[0]==1):
		     for i in range(len(data)):
			  if(int(i*amount)>(len(data)-1)):
			       break
			  count+=1
			  new.append(int(data[int(i*amount)]))
		else:
		     for i in range(0,len(data),2):
			  if(int(i*amount)>(len(data)-1)):
			       break
			  count+=1
			  new.append(int(data[int(i*amount)]))
			  if(int(i+1)*amount>(len(data)-1)):
			       new.append(0)
			  else:
			       new.append(int(data[int((i+1)*amount)]))


		self.parameters[3] = count
		self.data = tuple(new)
		self.parameters = tuple(self.parameters)



#     		SourceWaveFile = wave.open(SourceFile,'r')
 #    		parameters = SourceWaveFile.getparams()
  #   		print parameters
   #  		length = SourceWaveFile.getnframes()
    # 		waveData = SourceWaveFile.readframes(length)
     #		SourceWaveFile.close()
     #		DestinationWaveFile = wave.open(NewFile,'w')
    #		if(parameters[1]==2):
#		     var = '%ih' %(parameters[0]*parameters[3])
#     		else:
#		     var = '%iB' %(parameters[0]*parameters[3])
 #    		data = struct.unpack(var, waveData)
  #   		l=[]
#		i=0
#		factor = amount*1.0
#		var1 = factor*i
 #    		while(var1<len(data)):
#		     if(var1.is_integer()):
#			  for j in range(parameters[0]):
#			       l.append(data[int(var1)+j])
#		     else:
#			  for j in range(parameters[0]):
#			       l.append(0)
#		     #i+=parameters[0]
#		     var1=factor*i
#		print len(data)
#		print len(l)
 #    		parameters1=list(parameters)
#     		parameters1[3] = (parameters1[3]*(1.0))/amount
#		#if not parameters1[3].is_integer():
#		     parameters1[3]=int(parameters1[3])+1
#		else:
#		     parameters1[3]=int(parameters1[3])
#		parameters1 = tuple(parameters1)
#		print parameters1
#		print parameters1
 #   		if(parameters1[1]==2):
#		     var = '%ih' %(parameters1[0]*parameters1[3])
#     		else:
#		     var = '%iB' %(parameters1[0]*parameters1[3])
#
 #    		DestinationWaveFile.setparams(parameters1)
#     		newFile=struct.pack(var,*l)
#     		DestinationWaveFile.writeframes(newFile)
 #    		DestinationWaveFile.close()



        def Shift(self,SourceFile,amount,NewFile):
	     #	SourceWaveFile = wave.open(SourceFile,'r')
	#	parameters = SourceWaveFile.getparams()
	#	print parameters
	#	length = SourceWaveFile.getnframes()
	#	waveData = SourceWaveFile.readframes(length)
	#	SourceWaveFile.close()
	#	DestinationWaveFile = wave.open(NewFile,'w')
	#	if(parameters[1]==2):
	#	     var = '%ih' %(parameters[0]*parameters[3])
	#	else:
	#	     var = '%iB' %(parameters[0]*parameters[3])
	#	data = struct.unpack(var, waveData)
		extra_frames=0
		if(amount>0):
			extra_frames=int(self.parameters[2]*amount)
			l=[]
			for i in range(extra_frames):
		     		l.append(0)
		     		if(self.parameters[0]==2):
			  		l.append(0)
			for i in range(len(self.data)):
		     		l.append(int(self.data[i]))
			parameters1=list(self.parameters)
			print extra_frames
			parameters1[3]+=extra_frames
			parameters1=tuple(parameters1)
			print parameters1
    			if(parameters1[1]==2):
		     		var = '%ih' %(parameters1[0]*parameters1[3])
     			else:
		     		var = '%iB' %(parameters1[0]*parameters1[3])
			self.data = l
			self.parameters = parameters1
			self.var = var

	#		DestinationWaveFile.setparams(parameters1)
	#		newFile=struct.pack(var,*l)
	#		DestinationWaveFile.writeframes(newFile)
	#		DestinationWaveFile.close()
	        else:
		     l=[]
		     extra_frames =int(self.parameters[2]*abs(amount))
		     if(self.parameters[0]==1):
			  for i in range(extra_frames,len(self.data)):
			       l.append(self.data[i])
		     
		     elif(self.parameters[0]==2):
			  for i in range(2*extra_frames,len(self.data)):
			       l.append(self.data[i])
	             parameters1=list(self.parameters)
		     print extra_frames
		     parameters1[3]-=extra_frames
		     parameters1=tuple(parameters1)
		     print parameters1
    		     if(parameters1[1]==2):
		     		var = '%ih' %(parameters1[0]*parameters1[3])
     		     else:
		     		var = '%iB' %(parameters1[0]*parameters1[3])

		     self.data = l
		     self.parameters = parameters1
		     self.var = var
	#	     DestinationWaveFile.setparams(parameters1)
	#	     newFile=struct.pack(var,*l)
	#	     DestinationWaveFile.writeframes(newFile)
	#	     DestinationWaveFile.close()




	def Mix(self,SourceFile,NewFile):
	        SourceWaveFile=[]
		parameters=[]
		length=[]
		waveData=[]
		var=[]
		data=[]
		print SourceFile
		print NewFile
	     	for i in range(len(SourceFile)):
		     SourceWaveFile.append(self.OpenSourceFile(SourceFile[i]))
     		     parameters.append(SourceWaveFile[i].getparams())
     		     length.append(SourceWaveFile[i].getnframes())
		
		#SourceWaveFile2 = OpenSourceFile(SourceFile2)
		#parameters2 = SourceWaveFile2.getparams()
		#length2 = SourceWaveFile2.getnframes()
		parameters1=list(parameters[0])
		for i in range(len(SourceFile)):
		     waveData.append(SourceWaveFile[i].readframes(length[i]))
     		     SourceWaveFile[i].close()
    		# if(parameters[1]==2):
		for i in range(len(SourceFile)):
		     #      if(parameters[i][1]==2):
			    var.append('%ih' %(parameters[i][0]*parameters[i][3]))
		      # else:
		#	    var.append('%iB' %(parameters[i][0]*parameters[i][3]))
	        for i in range(len(SourceFile)):
		     data.append(struct.unpack(var[i], waveData[i]))
		n=1000000000000
		m=-1
		factor = ((1.0)/len(SourceWaveFile))
     		for i in range(len(SourceFile)):
		     n=min(n,len(data[i]))
		     m=max(m,(int(length[i])))
		print len(data[0]),length[0]
		print len(SourceFile)
		parameters1[3]=m
		print "HERE is M jnadslk andosamoida dansodnas"
		print m
		parameters1=tuple(parameters1)
     		l=[]
		print parameters[0]
		print parameters[1]
		print parameters1
     		for i in range(n):
		     temp=0
		     for j in range(len(SourceFile)):
			  temp+=factor*int(data[j][i])
	    	     l.append(int(temp))
		print len(l)
		if(parameters1[0]==2):
			for i in range(2*m-n):
		     		l.append(0)
		else:
			for i in range(m-n):
		     		l.append(0)


     		for i in range(len(l)):
	  		if(not(((int(l[i])))<=32767 and ((int(l[i])))>=-32767)):
	       			if(((int(l[i])))<0):
		    			l[i]=-32767
				else:
				     l[i]=32767
		
		print len(l) ,2*m
     		for i in range(len(l)):
	  		if(not(((int(l[i])))<=32767 and ((int(l[i])))>=-32767)):
	       			print "WRONG"
		#print l
		var1='%ih' %(parameters1[0]*parameters1[3])
		DestinationWaveFile = wave.open(NewFile,'w')
		self.parameters = parameters1
		DestinationWaveFile.setparams(parameters1)
		newFile=struct.pack(var1,*l)
		DestinationWaveFile.writeframes(newFile)
     		DestinationWaveFile.close()


		     
		     
#		l=[]
 #    		n=min(len(data1),len(data2))
  #   		for i in range(n):
#	  		l.append(data1[i]+data2[i])
 #    		if(len(data1)>len(data2)):
#	  		for i in range(len(data1)-n):
#	       			l.append(data1[i])
 #    		else:
#	  		for i in range(len(data2)-n):
#	       			l.append(data2[i])
 #    		for i in range(len(l)):
#	  		if(not(((int(l[i])))<=32767 and ((int(l[i])))>=-32767)):
#	       			if(((int(l[i])))<0):
#		    			l[i]=-32767
#	       			else:
		#    			l[i]=32767
		   
	       
	#	newFile=struct.pack(var1,*l)
	#	DestinationWaveFile.writeframes(newFile)
	#	DestinationWaveFile.close()


	def Modulate(self,SourceFile,NewFile):
	        SourceWaveFile=[]
		parameters=[]
		length=[]
		waveData=[]
		var=[]
		data=[]
		print "LENGTH OF SOURCE FILE"
		print len(SourceFile)
		print NewFile
	     	for i in range(len(SourceFile)):
		     SourceWaveFile.append(self.OpenSourceFile(SourceFile[i]))
     		     parameters.append(SourceWaveFile[i].getparams())
     		     length.append(SourceWaveFile[i].getnframes())
		
		#SourceWaveFile2 = OpenSourceFile(SourceFile2)
		#parameters2 = SourceWaveFile2.getparams()
		#length2 = SourceWaveFile2.getnframes()
		parameters1=list(parameters[0])
		for i in range(len(SourceFile)):
		     waveData.append(SourceWaveFile[i].readframes(length[i]))
     		     SourceWaveFile[i].close()
    		# if(parameters[1]==2):
		for i in range(len(SourceFile)):
		     #     if(parameters[i][1]==2):
			 var.append('%ih' %(parameters[i][0]*parameters[i][3]))
		    # else:
		#	  var.append('%iB' %(parameters[i][0]*parameters[i][3]))
	        for i in range(len(SourceFile)):
		     data.append(struct.unpack(var[i], waveData[i]))
		n=1000000000000
		m=-1
		for i in range(len(SourceFile)):
		     n=min(n,len(data[i]))
		     m=max(m,(int(length[i])))
		print len(data[0]),length[0]
		print len(SourceFile)
		parameters1[3]=m
		print m
		parameters1=tuple(parameters1)
     		l=[]
	#	print parameters[0]
	#	print parameters[1]
		print parameters1
     		for i in range(n):
		     temp=1
		     for j in range(len(SourceFile)):
			  temp*=int(data[j][i])
	    	     l.append(int(temp))
		print len(l)
		if(parameters1[0]==2):
			for i in range(2*m-n):
		     		l.append(0)
		else:
			for i in range(m-n):
		     		l.append(0)


     		for i in range(len(l)):
	  		if(not(((int(l[i])))<=32767 and ((int(l[i])))>=-32767)):
	       			if(((int(l[i])))<0):
		    			l[i]=-32767
				else:
				     l[i]=32767
		
		print len(l) ,2*m
     		for i in range(len(l)):
	  		if(not(((int(l[i])))<=32767 and ((int(l[i])))>=-32767)):
	       			print "WRONG"
		#print l
		var1='%ih' %(parameters1[0]*parameters1[3])
		DestinationWaveFile = wave.open(NewFile,'w')
		self.parameters = parameters1
		DestinationWaveFile.setparams(parameters1)
		newFile=struct.pack(var1,*l)
		DestinationWaveFile.writeframes(newFile)
     		DestinationWaveFile.close()





#a=dsaa()
#l=[]
#l.append('got.wav')
#l.append('bella.wav')
#a.Modulate(l,'temp3.wav')
#Mix('5.wav','GUNSHOT.WAV','test2.wav')

