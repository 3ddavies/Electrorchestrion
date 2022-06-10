"""
Test #6. Clean up code and start grouping midi commands.
Moving testing functions to other files to clean up and organize core code.

"""
from binascii import unhexlify
from mididictionaries import *
from MT6.inits import *
from MT6.listmidis import *
from mididatastruct1 import *

def cleanarray(gross):
	for i in range(0, gross.count('')):
		gross.remove('')
	return gross

def keysig(keybyte):
	return twoscomplement[int(keybyte, 16)]


def hexseperate(string):
	stringx = str(string.hex())
	return ' '.join(stringx[i:i+2] for i in range(0,len(stringx),2))

def hextobin(hexnum):
	return bin(int(str(hexnum).replace("b'","").replace("'",""), 16))[2:].zfill(16)

def timedivision(time):
	ttp = hextobin(time)
	#print(ttp)
	#print(type(ttp))
	if ttp[0] == '0':#time signature is in ticks per quarter note
		return int(ttp[1:], 2)
	elif ttp[0] == '1':
		print("Parsing frames per second will be added in a future update. Please try another MIDI file.")
		pass
	else:
		print("Can't determine time signature. Are you sure this is a valid MIDI file?")


def vlvcheck(ta):
	dtl = True#loop condition
	edt = ''#event delta time
	while dtl == True:
		tapoped=ta.pop(0)
		edt+=tapoped
		if int(tapoped, 16) < 128:#indicates that next value will not be  part of the vlv
			dtl = False
	return ta, edt



def EventParse(eventcode, data):
	pass







def mparse(stringcheese, TrackMidiEvents):
	#string cheese is the raw bytes read from the file
	UnparsedBytes = MidiBytes([(stringcheese[i:i+2]) for i in range(0, len(stringcheese), 2)])#splits the track string into an array of bytes.
	ta = UnparsedBytes.MidiByteArray
	#ta is an array of bytes like ['4a', '00', '40', '48', '06', '40']
	trackeventsarray = []#stores all events in a track.
	trackins=[]#instruments
	tchn = ''#trackname
	#TrackMidiEvents = MidiFile.MidiTracks("name",0)
	while len(ta) > 0:#while there are still bytes to read
		#NewEvent = TrackMidiEvents.AddTrackEvent()
		ta,edt = vlvcheck(ta)
		arb = []
		#ta[] is the byte array, while tapc is the position currently being read, therefore ta[tapc] represents the current byte being read.
		EventType = UnparsedBytes.ByteTop()
		if EventType == "ff":#indicates MIDI meta event
			UnparsedBytes.BytePop()
			rmc = UnparsedBytes.BytePop()
			if midimeta[rmc][2] == 'vlv':
				ta,vlvs = vlvcheck(ta)				
				eventlength = int(vlvs,16)#this will tell us how many bytes the event is.
			else:
				arb = UnparsedBytes.BytePop(midimeta[rmc][1])
				eventlength = midimeta[rmc][2]
			eventraw = UnparsedBytes.BytePop(eventlength)
			event = [edt, rmc, midimeta[rmc][0], arb, eventraw]
			if midimeta[rmc][3] == True:#if the event is a text event, append a string with the decoded ASCII to the array.
				event.append(unhexlify("".join(eventraw)).decode())
			elif rmc == "59":#if the event is a keysig event
				event.append(keysig(eventraw[0]))

			if rmc == "03":#Trackname 
				tchn = event[len(event)-1]
				TrackMidiEvents.Name = event[len(event)-1]
			trackeventsarray.append(event)

		elif EventType[0] in musicalevents:#if the event is a musical event:
			rmc=UnparsedBytes.BytePop()
			evdata = UnparsedBytes.BytePop(musicalevents[rmc[0]][1])
			event = [edt, rmc, 'Event "' + musicalevents[rmc[0]][0] + '" on channel ' + str(rmc[1]), [], evdata]
			trackeventsarray.append(event)
			if rmc[0] == "c":#patch change
					trackins.append([str(int(event[len(event)-1][0], 16)), midiprogs[str(int(event[len(event)-1][0], 16))],  str(rmc[1])])

		elif EventType in ["f0", "f7"]:#indicates Sysex event
			rmc=UnparsedBytes.BytePop()
			ta,vlvsa = vlvcheck(ta)
			eventlength = int(vlvsa,16)#this will tell us how many bytes the event is.
			eventraw = UnparsedBytes.BytePop(eventlength)
			event = [edt, rmc, "Sysex Event", [], eventraw]
			trackeventsarray.append(event)








		#poopy smelly








		else:#if there is no event code, we can assume that it is the same as the previous event's code.
			if rmc in midimeta:
				if midimeta[rmc][2] == 'vlv':
					ta,vlvs = vlvcheck(ta)
					eventlength = int(vlvs,16)#this will tell us how many bytes the event is.
				else:
					arb = UnparsedBytes.BytePop(midimeta[rmc][1])
					eventlength = midimeta[rmc][2]
				eventraw = UnparsedBytes.BytePop(eventlength)
				event = [edt, rmc, midimeta[rmc][0], arb, eventraw]
				if midimeta[rmc][3] == True:#if the event is a text event, append a string with the decoded ASCII to the array.
					try:
						event.append(unhexlify("".join(eventraw)).decode())
					except:
						verpri(event)
						exit()
				elif rmc == "59":#if the event is a keysig event
					event.append(keysig(eventraw[0]))
				trackeventsarray.append(event)
				
			elif rmc[0] in musicalevents:
				verpri('Event "' + musicalevents[rmc[0]][0] + '" on channel ' + str(rmc[1]))
				evdata = UnparsedBytes.BytePop(musicalevents[rmc[0]][1])
				event = [edt, rmc, 'Event "' + musicalevents[rmc[0]][0] + '" on channel ' + str(rmc[1]), [], evdata]
				trackeventsarray.append(event)
				if rmc[0] == "c":#patch change
					trackins.append(midiprogs[str(int(event[len(event)-1][0], 16))])
			else:
				print("stuck!", ta[0])
				print("EDT ", edt)
				print(rmc)
	print("TAL",len(ta))
	return trackeventsarray, trackins, tchn

#mba is the midi byte array
def FullParse(mba):
	mastertrackarray = []#this array will store all tracks in arrays. format will be [[track0size, track0], [track1size, track1], [track2size, track2]]
	mastereventarray = []#[[[]]]
	ChannelEventArray = []#[[],[],[]]
	TrackArray = []
	ParsedMidi = MidiFile() #create MidiFile object
	ParsedMidi.Header = mba.ByteRead(4)
	ParsedMidi.HeaderChunkLength = mba.ByteRead(4)
	ParsedMidi.MidiType = int(mba.ByteRead(2).hex(), 16)
	ParsedMidi.NumMTrkChunks = int(mba.ByteRead(2).hex(), 16)
	ParsedMidi.DeltaTimes = mba.ByteRead(2)#if no tempo is assigned, 120bpm is assumed.

	print(timedivision(ParsedMidi.DeltaTimes.hex()))

	print(ParsedMidi.Header)
	print(type(ParsedMidi.Header))
	print("Header: "+str(ParsedMidi.Header.decode("utf-8")))
	print("MThd chunk length: "+str(ParsedMidi.NumMTrkChunks))
	print("MIDI Format Type: "+str(ParsedMidi.MidiType))
	print("Number of MTrk chunks (number of tracks): "+str(ParsedMidi.NumMTrkChunks))



	print("Delta time: "+str(int(ParsedMidi.DeltaTimes.hex(), 16)))

	if hextobin(ParsedMidi.DeltaTimes.hex())[0] == '0':
		print("Time signature is in ticks per beat (quarter note)")
	elif hextobin(ParsedMidi.DeltaTimes.hex())[0] == '1':
		print("Time signature is in frames per second")
	else:
		print("Error: couldn't read the time division. Are you sure this is a valid MIDI file?")




	#the below will have to be repeated for each track in a midi file.

	#this is basically the track identifying itself and saying how long it is.

	"""
	next comes the track data. However it is possible for other data to be present like the song
	title or the author's name who created the midi file.

	In adition, how we proceed next depends on the type of midi file. In a type 0 midi there is only one MTrk
	chunk (one track), but in type one midis with multiple MTrk chunks (multiple tracks) the first MTrk chunk
	is a "global tempo track" and contains all timing related events, while subsequent tracks will contain
	note data and no timing events.

	#type 0 midis only have one MTrk chunk, so no recursion is required.
	#type 0 midis are also the most common type, followed by type 1.

	type 1 midis use the first MTrk chunk as the "global tempo track".

	first read the global tempo track, then recursivly read the rest of the tracks, that is, 
	range(0,numberofmtrkchunks-1)

	"""

	if ParsedMidi.MidiType == 0:
		print("type 0")

	elif ParsedMidi.MidiType == 1:
		print("type 1")

	elif ParsedMidi.MidiType == 2:#almost never used, this will be one of the last things to be done.
		print("Sorry, type 2 MIDIs aren't yet supported. Please try another MIDI file.")

	else:#if no type is detected, it's a bad midi file.
		print("Couldn't determine MIDI type. Are you sure this is a valid MIDI file?")


	for i in range(0, ParsedMidi.NumMTrkChunks):#for each track:
		trach = mba.ByteRead(4)
		bytesintrack = mba.ByteRead(4)
		tavern = mba.ByteRead(int(bytesintrack.hex(), 16))#raw track data
		tavern = tavern.hex()
		mastertrackarray.append([bytesintrack.hex(), tavern])
		ParsedMidi.AddTrack(None,bytesintrack.hex())
		mpr = mparse(tavern, ParsedMidi.Track(i))
		ParsedMidi.Track(i).RawTrack=mpr
		#ParsedMidi.Track(i).Name=mpr[2]
		mastereventarray.append(mpr[0])#track events
		ChannelEventArray.append(mpr[1])#instruments??
		TrackArray.append(mpr[2])#mpr[2]is the name of the track
		
	ParsedMidi.Track(0).Name = "global tempo track"

	print(ChannelEventArray)
	ChannelEventArray = cleanarray(ChannelEventArray)
	TrackArray = cleanarray(TrackArray)
	NewTrackArray = []
	for jkjkjk in TrackArray:
		NewTrackArray.append(jkjkjk.strip())
	"""
	print("MasterEventArray:")
	print(len(mastereventarray))
	#print(mastereventarray)
	print("ChannelEventArray:")
	print(ChannelEventArray)
	print("NewTrackArray:")
	print(NewTrackArray)
	print("TrackArray:")
	print(TrackArray)

	print(ParsedMidi.Tracks)
	"""
	for i in ParsedMidi.Tracks:
		print(i.Name)
		#print(i.RawTrack)
	print(ParsedMidi.NumMTrkChunks)
	
	#print(ParsedMidi.Track(2).RawTrack)
	
	return ParsedMidi

midibytearray = MidiBytes(openmidi(listmid()))#array that the bytes will be stored in.
FullParse(midibytearray)