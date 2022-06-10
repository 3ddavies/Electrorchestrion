import os
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