#FF indicates a meta event. The following dict is for the byte after FF:
#Format: title of event followed by how many bytes to read.
#Format: "ID":["Event Title", numofarbitrarybytes, numofbytes]
from mididictionaries import *
testarr = [['00000030', '00ff7f0d050f1c323030332e31322e303100ff7f08050f1200007f7f0000ff5103068a1a00ff58040402180800ff2f00']]
#test array from track 0 of a MIDI file.
#to access the track contents, testarr[trackindex][1]
tarp=0#track array position
def midieventparser():
	ta = [(y[i:i+2]) for i in range(0, len(y), 2)]#splits the track string into an array of bytes.
	tapc = 0#pos counter
	if ta[tapc] == "ff":#indicates MIDI meta event
		tapc+=1
		rmc = ta[tapc]#this is the identifier of the meta instruction.
		tapc+=1
		if midimeta[rmc][2] == 'vlv':
			print(True)

def midimetaevent():
	wtd = midimeta[]

#midimeta[i][2] == 'vlv'

#parsing VLVs
def vlv(hxv):
	if int(hxv, 16) >= 128:#if the decimal value of the byte is greater than 128, it means the next byte is also part of the vlv.
		return True
	else:
		return False


"""

def readbytefromstring():
	counter = 0
	for i in range(0, int(len(x[0][0])/2)):
		print(x[0][0][counter:counter+2])
		counter+=2
"""

def readbytefromstring(string, index):
	for i in range(0, int(len(string)/2)):
		print(string[index:index+2])