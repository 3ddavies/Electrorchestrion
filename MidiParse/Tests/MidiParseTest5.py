"""
Test #5. Clean up code and start grouping midi commands.

"""
import os
from binascii import unhexlify
from mididictionaries import *
import argparse
verbpa = argparse.ArgumentParser()
verbpa.add_argument('-v', '--verbose', action="store_true", help="enables verbose output (debug)")
vera = verbpa.parse_args()
if vera.verbose:
	def verpri(stuff):
		print(stuff)
else:
	def verpri(stuff):
		pass

def cleanarray(gross):
	for i in range(0, gross.count('')):
		gross.remove('')
	return gross


def fixtracknames(broken):
	fixed = []
	for tracktitle in tracknames:
			for instrument in insdict:
				if instrument in tnu:
					fixed.append(instrument)
	return fixed


def keysig(keybyte):
	return twoscomplement[int(keybyte, 16)]


def openmidi(file):
	tmbr = []
	f = open(file, "rb")#opening the midi in binary mode
	loopfile = True
	while loopfile == True:
		cb = f.read(1)
		if cb != b'':#checking if there are still bytes left to read
			tmbr.append(cb)
		else:
			loopfile = False
	return tmbr


def hexseperate(string):
	stringx = str(string.hex())
	return ' '.join(stringx[i:i+2] for i in range(0,len(stringx),2))


def byteread(num):#will read and return the specified number of bytes
	global bytecounter
	bytehold = b''
	for i in range(0, num):#reads specified number of bytes
		bytehold+=midibytearray[i+bytecounter]#number of increment plus the read position
	bytecounter+=num#after reading is done read position is incremented by the number of bytes read.
	return bytehold#after looping is done the specified bytes are returned.

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

def listmid():
	#ptmf = 'C:\\Users\\gabep\\Desktop\\Electrorchestrion\\Midis\\' old static path, replacing with dynamic path
	ptmf = os.getcwd().split("MidiParse\\Tests")[0]+"Midis\\"

	midifiles = []
	# r=root, d=directories, f = files
	for r, d, f in os.walk(ptmf):
		for file in f:
			if '.mid' in file:
				midifiles.append(file)

	print("Which MIDI file would you like to use?")
	for i in range(0,len(midifiles)):
		print(str(i)+" - "+str(midifiles[i]))

	ktfmi = True
	while ktfmi == True:
		try:
			return os.path.join(r, midifiles[int(input("->"))])
			ktfmi = False
		except:
			print("Error: your input should be a number from 0 to "+str(i)+".")


def mparse(stringcheese):
	ta = [(stringcheese[i:i+2]) for i in range(0, len(stringcheese), 2)]#splits the track string into an array of bytes.
	tapc = 0#pos counter
	trackeventsarray = []#stores all events in a track.
	trackins=[]#instruments
	tchn = ''

	while len(ta) > tapc:#while there are still bytes to read
		verpri('tapc '+str(tapc))
		dtl = True#loop condition
		edt = ''#event delta time
		while dtl == True:
			edt+=ta[tapc]
			if int(ta[tapc], 16) < 128:#indicates that next value will not be  part of the vlv
				dtl = False
			tapc+=1
			verpri("edt " +str(edt))
		arb = []
		if ta[tapc] == "ff":#indicates MIDI meta event
			tapc+=1
			rmc = ta[tapc]#this is the identifier of the meta instruction.
			verpri("RMC: "+str(rmc))
			tapc+=1
			if midimeta[rmc][2] == 'vlv':
				verpri(True)
				vlvl = True#loop condition
				vlvs = ''#vlv string
				while vlvl == True:
					vlvs+=ta[tapc]
					tapc+=1
					if int(ta[tapc], 16) < 128:#indicates that next value will not be  part of the vlv
						vlvl = False
				verpri(vlvs)
				verpri(int(vlvs,16))
				eventlength = int(vlvs,16)#this will tell us how many bytes the event is.
			else:
				for k in range(0,midimeta[rmc][1]):
					arb.append(ta[tapc])
					tapc+=1
				eventlength = midimeta[rmc][2]
			eventraw = []
			for j in range(0, eventlength):
				eventraw.append(ta[tapc])
				tapc+=1
			event = [edt, rmc, midimeta[rmc][0], arb, eventraw]
			if midimeta[rmc][3] == True:#if the event is a text event, append a string with the decoded ASCII to the array.
				event.append(unhexlify("".join(eventraw)).decode())
			elif rmc == "59":#if the event is a keysig event
				event.append(keysig(eventraw[0]))

			if rmc == "03":
				print("03 gabe ", event)
				tchn = event[len(event)-1]

			verpri(event)
			verpri(len(eventraw))
			trackeventsarray.append(event)

		elif ta[tapc][0] in musicalevents:#if the event is a musical event:
			rmc= ta[tapc]#event. rmc[0] will be the event name while rmc[1] is the channel.
			tapc+=1
			verpri("RMC: "+str(rmc))
			verpri('Event "' + musicalevents[rmc[0]][0] + '" on channel ' + str(rmc[1]))
			evdata = ta[tapc:tapc+musicalevents[rmc[0]][1]]
			tapc+=musicalevents[rmc[0]][1]
			event = [edt, rmc, 'Event "' + musicalevents[rmc[0]][0] + '" on channel ' + str(rmc[1]), [], evdata]
			verpri(event)
			trackeventsarray.append(event)
			if rmc[0] == "c":#patch change
					trackins.append([str(int(event[len(event)-1][0], 16)), midiprogs[str(int(event[len(event)-1][0], 16))],  str(rmc[1])])

		elif ta[tapc] in ["f0", "f7"]:#indicates Sysex event
			rmc = ta[tapc]#this is the identifier of the meta instruction.
			tapc+=1
			vlvla = True#loop condition
			vlvsa = ''#vlv string
			while vlvla == True:
				vlvsa+=ta[tapc]
				tapc+=1
				if int(ta[tapc], 16) < 128:#indicates that next value will not be  part of the vlv
					vlvla = False
				verpri(vlvsa)
				verpri(int(vlvsa,16))
			eventlength = int(vlvsa,16)#this will tell us how many bytes the event is.
			eventraw = []
			for fj in range(0, eventlength):
				eventraw.append(ta[tapc])
				tapc+=1
			event = [edt, rmc, "Sysex Event", [], eventraw]
			verpri(event)
			verpri(len(eventraw))
			trackeventsarray.append(event)
			#tapc+=1





		else:#if there is no event code, we can assume that it is the same as the previous event's code.
			if rmc in midimeta:
				if midimeta[rmc][2] == 'vlv':
					verpri(True)
					vlvl = True#loop condition
					vlvs = ''#vlv string
					while vlvl == True:
						vlvs+=ta[tapc]
						tapc+=1
						if int(ta[tapc], 16) < 128:#indicates that next value will not be  part of the vlv
							vlvl = False
					verpri(vlvs)
					verpri("event length", int(vlvs,16))
					verpri("event length", vlvs)
					eventlength = int(vlvs,16)#this will tell us how many bytes the event is.
				else:
					for lll in range(0,midimeta[rmc][1]):
						arb.append(ta[tapc])
						tapc+=1
					eventlength = midimeta[rmc][2]
				eventraw = []
				for jjj in range(0, eventlength):
					eventraw.append(ta[tapc])
					tapc+=1
				event = [edt, rmc, midimeta[rmc][0], arb, eventraw]
				if midimeta[rmc][3] == True:#if the event is a text event, append a string with the decoded ASCII to the array.
					try:
						event.append(unhexlify("".join(eventraw)).decode())
					except:
						#verpri(eventraw)
						verpri(event)
						exit()
				elif rmc == "59":#if the event is a keysig event
					event.append(keysig(eventraw[0]))
				verpri(event)
				verpri(len(eventraw))
				trackeventsarray.append(event)
				verpri("SPECIAL EVENT")
				#exit()

			elif rmc[0] in musicalevents:
				verpri('Event "' + musicalevents[rmc[0]][0] + '" on channel ' + str(rmc[1]))
				evdata = ta[tapc:tapc+musicalevents[rmc[0]][1]]
				tapc+=musicalevents[rmc[0]][1]
				event = [edt, rmc, 'Event "' + musicalevents[rmc[0]][0] + '" on channel ' + str(rmc[1]), [], evdata]
				verpri(event)
				trackeventsarray.append(event)
				verpri("SPECIAL EVENT")
				#exit()
				if rmc[0] == "c":#patch change
					trackins.append(midiprogs[str(int(event[len(event)-1][0], 16))])


			else:
				print("stuck!", ta[tapc])
				print("EDT ", edt)
				print(rmc)
				#exit()
	print("TAPC ", tapc)
	print("TAL",len(ta))
	return trackeventsarray, trackins, tchn




global bytecounter
bytecounter = 0 #keeps track of what position in the file is being read.

mastertrackarray = []#this array will store all tracks in arrays. format will be [[track0size, track0], [track1size, track1], [track2size, track2]]
mastereventarray = []#[[[]]]
ChannelEventArray = []#[[],[],[]]
TrackArray = []
midibytearray = openmidi(listmid())#array that the bytes will be stored in.




header = byteread(4)
chunklength = byteread(4)
formattype = byteread(2)
numofmtrkchunks = byteread(2)
deltatime = byteread(2)#if no tempo is assigned, 120bpm is assumed.
#print(deltatime.hex())

print(timedivision(deltatime.hex()))

print(header)
print(type(header))
print("Header: "+str(header.decode("utf-8")))
print("MThd chunk length: "+str(int(chunklength.hex(), 16)))
print("MIDI Format Type: "+str(int(formattype.hex(), 16)))
print("Number of MTrk chunks (number of tracks): "+str(int(numofmtrkchunks.hex(), 16)))



print("Delta time: "+str(int(deltatime.hex(), 16)))

if hextobin(deltatime.hex())[0] == '0':
	print("Time signature is in ticks per beat (quarter note)")
elif hextobin(deltatime.hex())[0] == '1':
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
"""

if int(formattype.hex(), 16) == 0:#type 0 midis only have one MTrk chunk, so no recursion is required.
	print("type 0")#type 0 midis are also the most common type, followed by type 1.
	trach = byteread(4)
	bytesintrack = byteread(4)
	alcool = byteread(int(bytesintrack.hex(), 16)).hex()
	mastertrackarray.append([bytesintrack.hex(), alcool])
	mpr = mparse(alcool)
	mastereventarray.append(mpr[0])
	ChannelEventArray.append(mpr[1])
	TrackArray.append(mpr[2])

elif int(formattype.hex(), 16) == 1:#type 1 midis use the first MTrk chunk as the "global tempo track".
	print("type 1")
	
	for i in range(0, int(numofmtrkchunks.hex(), 16)):#for each track:
		trach = byteread(4)
		bytesintrack = byteread(4)
		tavern = byteread(int(bytesintrack.hex(), 16)).hex()
		mastertrackarray.append([bytesintrack.hex(), tavern])
		mpr = mparse(tavern)
		mastereventarray.append(mpr[0])
		ChannelEventArray.append(mpr[1])
		TrackArray.append(mpr[2])

#first read the global tempo track, then recursivly read the rest of the tracks, that is, 
#range(0,numberofmtrkchunks-1)


elif int(formattype.hex(), 16) == 2:#almost never used, this will be one of the last things to be done.
	print("Sorry, type 2 MIDIs aren't yet supported. Please try another MIDI file.")

else:#if no type is detected, it's a bad midi file.
	print("Couldn't determine MIDI type. Are you sure this is a valid MIDI file?")

#print(int(numofmtrkchunks.hex(), 16))
#exit()
print(ChannelEventArray)
ChannelEventArray = cleanarray(ChannelEventArray)
TrackArray = cleanarray(TrackArray)
NewTrackArray = []
for jkjkjk in TrackArray:
	NewTrackArray.append(jkjkjk.strip())
"""
print("MasterEventArray:")
print(mastereventarray)
print("ChannelEventArray:")
print(ChannelEventArray)
print("NewTrackArray:")
print(NewTrackArray)
print("TrackArray:")
print(TrackArray)
"""