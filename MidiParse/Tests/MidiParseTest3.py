"""
Test #3. Building on test #2, test #3 will loop through tracks to read and store track data in an array.
"""

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

def timetype(deltatimebytes):#used to determine if the time division is in ticks per beat or frames per second.
	if str(deltatimebytes).replace("b'","").replace("'","")[0:2] == "00":
		return True#if true the time division is in ticks per beat.
	else:
		return False#the time division is in frames per second.

global bytecounter
bytecounter = 0 #keeps track of what position in the file is being read.

midibytearray = openmidi("C:\\Users\\gabep\\Desktop\\Electrorchestrion\\Midis\\EMMYLOU_HARRIS_-_Mr_Sandman.mid") #array that the bytes will be stored in.


#print(midibytearray)
#print(midibytearray[0])
#print(type(midibytearray[0]))



header = byteread(4)
chunklength = byteread(4)
formattype = byteread(2)
numofmtrkchunks = byteread(2)
deltatime = byteread(2)

print("Header: "+str(header.decode("utf-8")))
print("MThd chunk length: "+str(int(chunklength.hex(), 16)))
print("Midi Format Type: "+str(int(formattype.hex(), 16)))
print("Number of MTrk chunks (number of tracks): "+str(int(numofmtrkchunks.hex(), 16)))
print("Delta time: "+str(int(deltatime.hex(), 16)))
if timetype(deltatime.hex()) == True:
	print("Time signature is in ticks per beat")
else:
	print("Time signature is in frames per second")


#the below will have to be repeated for each track in a midi file.

#this is basically the track identifying itself and saying how long it is.

trach = byteread(4)
bytesintrack = byteread(4)
"""
next comes the track data. However it is possible for other data to be present like the song
title or the author's name who created the midi file.

In adition, how we proceed next depends on the type of midi file. In a type 0 midi there is only one MTrk
chunk (one track), but in type one midis with multiple MTrk chunks (multiple tracks) the first MTrk chunk
is a "global tempo track" and contains all timing related events, while subsequent tracks will contain
note data and no timing events.
"""

if int(formattype.hex(), 16) == 0:#type 0 midis only have one MTrk chunk, so no recursion is required.
	pass

elif int(formattype.hex(), 16) == 1:#type 1 midis use the first MTrk chunk as the "global tempo track".
	pass
#first read the global tempo track, then recursivly read the rest of the tracks, that is, 
#range(0,numberofmtrkchunks-1)


elif int(formattype.hex(), 16) == 2:#almost never used, this will be one of the last things to be done.
	print("Sorry, type 2 midis aren't yet supported. Please try another midi file.")

else:#if no type is detected, it's a bad midi file.
	print("Couldn't determine midi type. Are you sure this is a valid midi file?")


nt1 = byteread(1)
timesigme = byteread(7)
nt2 = byteread(1)
keysigme = byteread(5)
nt3 = byteread(1)

print("\n----------\n")

print("Track: "+str(trach.decode("utf-8")))
print("Number of bytes in track (chunk size): "+str(int(bytesintrack.hex(), 16)))
print("0 ticks")
print("Time signature meta event: "+hexseperate(timesigme))
print("0 ticks")
print("Key signature meta event: "+hexseperate(keysigme))
print("0 ticks")