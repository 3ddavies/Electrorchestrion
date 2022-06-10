class MidiBytes:
	"""class to store MidiBytes info and related functions"""

	def __init__(self, mba):
		self.MidiByteArray=mba
		#self.ByteCount = 0

	def ByteRead(self, num):#will read and return the specified number of bytes
		bytehold = b''
		for i in range(0, num):#reads specified number of bytes
			#bytehold+=self.MidiByteArray[i+self.ByteCount]#number of increment plus the read position
			bytehold+=self.MidiByteArray.pop(0)
		#self.ByteCount+=num#after reading is done read position is incremented by the number of bytes read.
		return bytehold#after looping is done the specified bytes are returned.
	
	def BytePop(self, num=1):#will read, pop and return the specified number of bytes
		
		if num==1:
			return self.MidiByteArray.pop(0)
		else:
			bytehold = []
			for i in range(0, num):#reads specified number of bytes
				#bytehold+=self.MidiByteArray[i+self.ByteCount]#number of increment plus the read position
				bytehold.append(self.MidiByteArray.pop(0))
			#self.ByteCount+=num#after reading is done read position is incremented by the number of bytes read.
			return bytehold#after looping is done the specified bytes are returned.

	def ByteTop(self, num=1):#will read and return the specified number of bytes
		
		if num==1:
			return self.MidiByteArray[0]
		else:
			bytehold = []
			for i in range(0, num):#reads specified number of bytes
				#bytehold+=self.MidiByteArray[i+self.ByteCount]#number of increment plus the read position
				bytehold.append(self.MidiByteArray[i])
			#self.ByteCount+=num#after reading is done read position is incremented by the number of bytes read.
			return bytehold#after looping is done the specified bytes are returned.



class MidiFile:
	"""Data structure to organize MIDI file data"""
	class MidiTracks:
		"""Data structire of MIDI Tracks"""
		#Note: Tracks are like the instruments (piano, sax, etc). While channels are where the note data is transmitted (i.e. left hand piano on channel 0, right hand on channel 1).
		class MtrkEvent:
			"""Mtrk Events"""

			def DecodeEvent(self):
				"""Outputs what the event is/does."""
				pass

			def __init__(self, dt, event, EventType):
				self.DeltaTime = dt
				self.RawEvent = event#full raw event, i.e. FF 01 ...
				self.EventType = EventType#f0 or f7 = Sysex Event, ff = Meta event, most else is Midi event.

		def AddTrackEvent(self, dt, event):
			self.MidiEvents.append(MtrkEvent(self, dt, event))

		def __len__(self):
			return self.Length


		def __init__(self, tname, le):
			self.Name = tname
			self.Length = le
			self.MidiEvents = []
			self.RawTrack = []
			self.CleanTrack = []

	def Track(self, n):
		"""returns a specific track"""
		return self.Tracks[n]

	def AddTrack(self, tname, le):
		"""Adds a MidiTrack object to the MidiFile object"""
		self.Tracks.append(self.MidiTracks(tname,le))
		#self.NumTracks+=1



	#__slots__ = "_NumTracks", "_MidiType", "_DeltaTimes", "_HeaderChunkLength"
	def __init__(self):
		self.Header = ""
		self.HeaderChunkLength = -1
		self.NumTracks = 0
		self.NumMTrkChunks = 0
		self.MidiType = -1 #-1 is an invalid value, so if -1 is read as the file after data input we can take this as a sign that the data was not entered into the structure correctly.
		self.DeltaTimes = -1
		self.Tracks = []
