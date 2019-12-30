import os

ptmf = 'C:\\Users\\gabep\\Desktop\\Electrorchestrion\\Midis\\'

midifiles = []
# r=root, d=directories, f = files
for r, d, f in os.walk(ptmf):
	for file in f:
		if '.mid' in file:
			midifiles.append(file)
#os.path.join(r, file)
'''
for f in files:
	print(f)
'''
#print(files)
print("Which MIDI file would you like to use?")
for i in range(0,len(midifiles)):
	print(str(i)+" - "+str(midifiles[i]))
mc = int(input("->"))
print(os.path.join(r, midifiles[mc]))