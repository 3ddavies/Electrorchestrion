"""
A good first test. the problem with this approach though is that f.read can't read backwards.

The next test will read the entire MIDI file and seperate it into an array of bytes.

"""
def hexseperate(string):
	stringx= str(string.hex())
	return ' '.join(stringx[i:i+2] for i in range(0,len(stringx),2))

f = open("C:\\Users\\gabep\\Desktop\\Electrorchestrion\\Midis\\BONEY M.Rasputin K.mid", "rb")

#f.readlines()

header = f.read(4)
chunklength = f.read(4)
formattype = f.read(2)
numofmtrkchunks = f.read(2)
deltatime = f.read(2)

print("Header: "+str(header.decode("utf-8")))
print("MThd chunk length: "+str(int(chunklength.hex(), 16)))
print("Midi Format Type: "+str(int(formattype.hex(), 16)))
print("Number of MTrk chunks: "+str(int(numofmtrkchunks.hex(), 16)))
print("Delta time: "+str(int(deltatime.hex(), 16)))


trach = f.read(4)
bytesintrack = f.read(4)
nt1 = f.read(1)
timesigme = f.read(7)
nt2 = f.read(1)
keysigme = f.read(5)
nt3 = f.read(1)
print("Track: "+str(trach.decode("utf-8")))
print("Number of bytes in track: "+str(int(bytesintrack.hex(), 16)))
print("0 ticks")
print("Time signature meta event: "+hexseperate(timesigme))
print("0 ticks")
print("Key signature meta event: "+hexseperate(keysigme))
print("0 ticks")