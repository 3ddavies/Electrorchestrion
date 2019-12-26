"""
Test #2. This test will first read over the entire file and seperate it into an array, byte by byte.
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

midibytearray = openmidi("C:\\Users\\gabep\\Desktop\\Electrorchestrion\\Midis\\BONEY M.Rasputin K.mid") #array that the bytes will be stored in.


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
trach = byteread(4)
bytesintrack = byteread(4)
nt1 = byteread(1)
timesigme = byteread(7)
nt2 = byteread(1)
keysigme = byteread(5)
nt3 = byteread(1)
print("Track: "+str(trach.decode("utf-8")))
print("Number of bytes in track: "+str(int(bytesintrack.hex(), 16)))
print("0 ticks")
print("Time signature meta event: "+hexseperate(timesigme))
print("0 ticks")
print("Key signature meta event: "+hexseperate(keysigme))
print("0 ticks")