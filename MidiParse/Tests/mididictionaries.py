midimeta = {
"00":["Sequence Number", 1, 2, False],
"01":["Text Event", 0, 'vlv', True],
"02":["Copyright Notice", 0, 'vlv', True],
"03":["Sequence/Track Name", 0, 'vlv', True],
"04":["Instrument Name", 0, 'vlv', True],
"05":["Lyric", 0, 'vlv', True], 
"06":["Marker", 0, 'vlv', True], 
"07":["Cue Point ", 0, 'vlv', True],
"20":["MIDI Channel Prefix", 1, 1, False],
"2f":["End of Track", 1, 0, False],
"51":["Set Tempo", 1, 3, False],
"54":["SMPTE Offset", 1, 5, False],
"58":["Time Signature", 1, 4, False],
"59":["Key Signature", 1, 2, False],
"7f":["Sequencer-Specific Meta-Event", 0, 'vlv', False]
}
"""
Command	Meaning				# parameters	param 1			param 2
0x80	Note-off				2			key				velocity
0x90	Note-on					2			key				veolcity
0xA0	Aftertouch				2			key				touch
0xB0	Continuous controller	2			controller #	controller value
0xC0	Patch Change			2			instrument #	
0xD0	Channel Pressure		1			pressure
0xE0	Pitch bend				2			lsb (7 bits)	msb (7 bits)
"""
#print(musicevents[bytestring[0]][0] + " on channel "+str(bytestring[1]))
musicalevents = {
"8":["Note Off", 2],
"9":["Note On", 2],
"a":["Aftertouch", 2],
"b":["Continuous Controller", 2],
"c":["Patch Change", 1],
"d":["Channel Pressure", 1],
"e":["Pitch Bend", 2]
}
#ff59 0203 00
keysignaturesf = {
""
}
twoscomplement = {
	
}

def twoispretty(uwu):
	return "1".join(bin(int(uwu,16))[2:].replace("0", "e").replace("1","0").replace("e", "1").rsplit("0", 1))	
#return rreplace(bin(int(uwu,16))[2:].replace("0", "e").replace("1","0").replace("e", "1"))


"""
def rreplace(s):
	li = s.rsplit("0", 1)
	return "1".join(li)
"""
"""
,
"f":["(non-musical commands)", ]
"""