midimeta = {
"00":["Sequence Number", 1, 2],
"01":["Text Event", 0, 'vlv'],
"02":["Copyright Notice", 0, 'vlv'],
"03":["Sequence/Track Name", 0, 'vlv'],
"04":["Instrument Name", 0, 'vlv'],
"05":["Lyric", 0, 'vlv'], 
"06":["Marker", 0, 'vlv'], 
"07":["Cue Point ", 0, 'vlv'],
"20":["MIDI Channel Prefix", 1, 1],
"2f":["End of Track", 1, 0],
"51":["Set Tempo", 1, 3],
"54":["SMPTE Offset", 1, 5],
"58":["Time Signature", 1, 4],
"59":["Key Signature", 1, 2],
"7f":["Sequencer-Specific Meta-Event", 0, 'vlv']
}

y = '00ff7f0d050f1c323030332e31322e303100ff7f08050f1200007f7f0000ff5103068a1a00ff58040402180800ff2f00'
#####00ff7f0d050f1c323030332e31322e303100ff7f08050f1200007f7f0000ff5103068a1a00ff58040402180800ff2f00
ta = [(y[i:i+2]) for i in range(0, len(y), 2)]#splits the track string into an array of bytes.
tapc = 1#pos counter
trackeventsarray = []#stores all events in a track.
while len(ta) > tapc:
	print('tapc '+str(tapc))
	if ta[tapc] == "ff":#indicates MIDI meta event
		tapc+=1
		rmc = ta[tapc]#this is the identifier of the meta instruction.
		tapc+=1
		if midimeta[rmc][2] == 'vlv':
			print(True)
			vlvl = True#loop condition
			vlvs = ''#vlv string
			while vlvl == True:
				vlvs+=ta[tapc]
				tapc+=1
				if int(ta[tapc], 16) < 128:#indicates that next value will not be  part of the vlv
					vlvl = False

			eventlength = int(vlvs,16)#this will tell us how many bytes the event is.
		else:
			tapc +=midimeta[rmc][1]#this will insure arbitrary bytes are ignored.
			eventlength = midimeta[rmc][2]
			
		eventraw = []
		for j in range(0, eventlength):
			eventraw.append(ta[tapc])
			tapc+=1
		event = [rmc, midimeta[rmc][0], eventraw]
		print(vlvs)
		print(int(vlvs,16))
		print(event)
		print(len(eventraw))
		tapc+=1#this is to avoid needlessly reading the '00' that preceeds FF.
		trackeventsarray.append(event)
	else:
		print("stuck!", ta[tapc])
		exit()
print(trackeventsarray)