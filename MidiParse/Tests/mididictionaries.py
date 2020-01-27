midimeta = {
"00":["Sequence Number", 1, 2, False],
"01":["Text Event", 0, 'vlv', True],
"02":["Copyright Notice", 0, 'vlv', True],
"03":["Sequence/Track Name", 0, 'vlv', True],
"04":["Instrument Name", 0, 'vlv', True],
"05":["Lyric", 0, 'vlv', True], 
"06":["Marker", 0, 'vlv', True], 
"07":["Cue Point", 0, 'vlv', True],
"08":["Program Name", 0, 'vlv', True],
"20":["MIDI Channel Prefix", 1, 1, False],
"21":["MIDI Port", 1, 1, False],
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

twoscomplement = {
249:-7,
250:-6,
251:-5,
252:-4,
253:-3,
254:-2,
255:-1,
0:0,
1:1,
2:2,
3:3,
4:4,
5:5,
6:6,
7:7
}


midiprogs = {	
"0": "Acoustic Grand Piano",
"1": "Bright Acoustic Piano",
"2": "Electric Grand Piano",
"3": "Honky-tonk Piano",
"4": "Electric Piano 1",
"5": "Electric Piano 2",
"6": "Harpsichord",
"7": "Clavi",
"8": "Celesta",
"9": "Glockenspiel",
"10": "Music Box",
"11": "Vibraphone",
"12": "Marimba",
"13": "Xylophone",
"14": "Tubular Bells",
"15": "Dulcimer",
"16": "Drawbar Organ",
"17": "Percussive Organ",
"18": "Rock Organ",
"19": "Church Organ",
"20": "Reed Organ",
"21": "Accordion",
"22": "Harmonica",
"23": "Tango Accordion",
"24": "Acoustic Guitar (nylon)",
"25": "Acoustic Guitar (steel)",
"26": "Electric Guitar (jazz)",
"27": "Electric Guitar (clean)",
"28": "Electric Guitar (muted)",
"29": "Overdriven Guitar",
"30": "Distortion Guitar",
"31": "Guitar harmonics",
"32": "Acoustic Bass",
"33": "Electric Bass (finger)",
"34": "Electric Bass (pick)",
"35": "Fretless Bass",
"36": "Slap Bass 1",
"37": "Slap Bass 2",
"38": "Synth Bass 1",
"39": "Synth Bass 2",
"40": "Violin",
"41": "Viola",
"42": "Cello",
"43": "Contrabass",
"44": "Tremolo Strings",
"45": "Pizzicato Strings",
"46": "Orchestral Harp",
"47": "Timpani",
"48": "String Ensemble 1",
"49": "String Ensemble 2",
"50": "SynthStrings 1",
"51": "SynthStrings 2",
"52": "Choir Aahs",
"53": "Voice Oohs",
"54": "Synth Voice",
"55": "Orchestra Hit",
"56": "Trumpet",
"57": "Trombone",
"58": "Tuba",
"59": "Muted Trumpet",
"60": "French Horn",
"61": "Brass Section",
"62": "SynthBrass 1",
"63": "SynthBrass 2",
"64": "Soprano Sax",
"65": "Alto Sax",
"66": "Tenor Sax",
"67": "Baritone Sax",
"68": "Oboe",
"69": "English Horn",
"70": "Bassoon",
"71": "Clarinet",
"72": "Piccolo",
"73": "Flute",
"74": "Recorder",
"75": "Pan Flute",
"76": "Blown Bottle",
"77": "Shakuhachi",
"78": "Whistle",
"79": "Ocarina",
"80": "Lead 1 (square)",
"81": "Lead 2 (sawtooth)",
"82": "Lead 3 (calliope)",
"83": "Lead 4 (chiff)",
"84": "Lead 5 (charang)",
"85": "Lead 6 (voice)",
"86": "Lead 7 (fifths)",
"87": "Lead 8 (bass + lead)",
"88": "Pad 1 (new age)",
"89": "Pad 2 (warm)",
"90": "Pad 3 (polysynth)",
"91": "Pad 4 (choir)",
"92": "Pad 5 (bowed)",
"93": "Pad 6 (metallic)",
"94": "Pad 7 (halo)",
"95": "Pad 8 (sweep)",
"96": "FX 1 (rain)",
"97": "FX 2 (soundtrack)",
"98": "FX 3 (crystal)",
"99": "FX 4 (atmosphere)",
"100": "FX 5 (brightness)",
"101": "FX 6 (goblins)",
"102": "FX 7 (echoes)",
"103": "FX 8 (sci-fi)",
"104": "Sitar",
"105": "Banjo",
"106": "Shamisen",
"107": "Koto",
"108": "Kalimba",
"109": "Bag pipe",
"110": "Fiddle",
"111": "Shanai",
"112": "Tinkle Bell",
"113": "Agogo",
"114": "Steel Drums",
"115": "Woodblock",
"116": "Taiko Drum",
"117": "Melodic Tom",
"118": "Synth Drum",
"119": "Reverse Cymbal",
"120": "Guitar Fret Noise",
"121": "Breath Noise",
"122": "Seashore",
"123": "Bird Tweet",
"124": "Telephone Ring",
"125": "Helicopter",
"126": "Applause",
"127": "Gunshot"
}

"""
MIDI Control Table
2nd byte	Function				3rd byte
0x00	Continuous controller #0	0-127, MSB
0x01	Modulation wheel			0-127, MSB
0x02	Breath control				0-127, MSB
0x03	Continuous controller #3	0-127, MSB
0x04	Foot controller				0-127, MSB
0x05	Portamento time				0-127, MSB
0x06	Data Entry					0-127, MSB
0x07	Main Volume					0-127, MSB
0x08	Continuous controller #8	0-127, MSB
0x09	Continuous controller #9	0-127, MSB
0x0A	Continuous controller #10	0-127, MSB
0x0B	Continuous controller #11	0-127, MSB
0x0C	Continuous controller #12	0-127, MSB
0x0D	Continuous controller #13	0-127, MSB
0x0E	Continuous controller #14	0-127, MSB
0x0F	Continuous controller #15	0-127, MSB
0x10	Continuous controller #16	0-127, MSB
0x11	Continuous controller #17	0-127, MSB
0x12	Continuous controller #18	0-127, MSB
0x13	Continuous controller #19	0-127, MSB
0x14	Continuous controller #20	0-127, MSB
0x15	Continuous controller #21	0-127, MSB
0x16	Continuous controller #22	0-127, MSB
0x17	Continuous controller #23	0-127, MSB
0x18	Continuous controller #24	0-127, MSB
0x19	Continuous controller #25	0-127, MSB
0x1A	Continuous controller #26	0-127, MSB
0x1B	Continuous controller #27	0-127, MSB
0x1C	Continuous controller #28	0-127, MSB
0x1D	Continuous controller #29	0-127, MSB
0x1E	Continuous controller #30	0-127, MSB
0x1F	Continuous controller #31	0-127, MSB
0x20	Continuous controller #0	0-127, LSB
0x21	Modulation wheel			0-127, LSB
0x22	Breath control				0-127, LSB
0x23	Continuous controller #3	0-127, LSB
0x24	Foot controller				0-127, LSB
0x25	Portamento time				0-127, LSB
0x26	Data entry					0-127, LSB
0x27	Main volume					0-127, LSB
0x28	Continuous controller #8	0-127, LSB
0x29	Continuous controller #9	0-127, LSB
0x2A	Continuous controller #10	0-127, LSB
0x2B	Continuous controller #11	0-127, LSB
0x2C	Continuous controller #12	0-127, LSB
0x2D	Continuous controller #13	0-127, LSB
0x2E	Continuous controller #14	0-127, LSB
0x2F	Continuous controller #15	0-127, LSB
0x30	Continuous controller #16	0-127, LSB
0x31	Continuous controller #17	0-127, LSB
0x32	Continuous controller #18	0-127, LSB
0x33	Continuous controller #19	0-127, LSB
0x34	Continuous controller #20	0-127, LSB
0x35	Continuous controller #21	0-127, LSB
0x36	Continuous controller #22	0-127, LSB
0x37	Continuous controller #23	0-127, LSB
0x38	Continuous controller #24	0-127, LSB
0x39	Continuous controller #25	0-127, LSB
0x3A	Continuous controller #26	0-127, LSB
0x3B	Continuous controller #27	0-127, LSB
0x3C	Continuous controller #28	0-127, LSB
0x3D	Continuous controller #29	0-127, LSB
0x3E	Continuous controller #30	0-127, LSB
0x3F	Continuous controller #31	0-127, LSB
0x40	Damper pedal on/off (Sustain)	0=off, 127=on
0x41	Portamento on/off			0=off, 127=on
0x42	Sustenuto on/off			0=off, 127=on
0x43	Soft pedal on/off			0=off, 127=on
0x44	Undefined on/off			0=off, 127=on
0x45	Undefined on/off			0=off, 127=on
0x46	Undefined on/off			0=off, 127=on
0x47	Undefined on/off			0=off, 127=on
0x48	Undefined on/off			0=off, 127=on
0x49	Undefined on/off			0=off, 127=on
0x4A	Undefined on/off			0=off, 127=on
0x4B	Undefined on/off			0=off, 127=on
0x4C	Undefined on/off			0=off, 127=on
0x4D	Undefined on/off			0=off, 127=on
0x4E	Undefined on/off			0=off, 127=on
0x4F	Undefined on/off			0=off, 127=on
0x50	Undefined on/off			0=off, 127=on
0x51	Undefined on/off			0=off, 127=on
0x52	Undefined on/off			0=off, 127=on
0x53	Undefined on/off			0=off, 127=on
0x54	Undefined on/off			0=off, 127=on
0x55	Undefined on/off			0=off, 127=on
0x56	Undefined on/off			0=off, 127=on
0x57	Undefined on/off			0=off, 127=on
0x58	Undefined on/off			0=off, 127=on
0x59	Undefined on/off			0=off, 127=on
0x5A	Undefined on/off			0=off, 127=on
0x5B	Undefined on/off			0=off, 127=on
0x5C	Undefined on/off			0=off, 127=on
0x5D	Undefined on/off			0=off, 127=on
0x5E	Undefined on/off			0=off, 127=on
0x5F	Undefined on/off			0=off, 127=on
0x60	Data entry +1					127
0x61	Data entry -1					127
0x62	Undefined	-
0x63	Undefined	-
0x64	Undefined	-
0x65	Undefined	-
0x66	Undefined	-
0x67	Undefined	-
0x67	Undefined	-
0x67	Undefined	-
0x67	Undefined	-
0x67	Undefined	-
0x68	Undefined	-
0x69	Undefined	-
0x6A	Undefined	-
0x6B	Undefined	-
0x6C	Undefined	-
0x6D	Undefined	-
0x6E	Undefined	-
0x6F	Undefined	-
0x70	Undefined	-
0x71	Undefined	-
0x72	Undefined	-
0x73	Undefined	-
0x74	Undefined	-
0x75	Undefined	-
0x76	Undefined	-
0x77	Undefined	-
0x78	Undefined	-
0x79	Undefined	-
0x7A	Local control on/off	0=off 127=on
0x7B	All notes off	0
0x7C	Omni mode off (includes all notes off)	0
0x7D	Omni mode on (includes all notes off)	0
0x7E	Poly mode on/off(includes all notes off)	**
0x7F	Poly mode on(incl mono=off&all notes off)	0
**Note:
This equals the number of channels, or zero if the number of channels equals the number of voices in the receiver.

"""

"""

"-7":["249", "f9", "11111001"],
"-6":["250", "fa", "11111010"],
"-5":["251", "fb", "11111011"],
"-4":["252", "fc", "11111100"],
"-3":["253", "fd", "11111101"],
"-2":["254", "fe", "11111110"],
"-1":["255", "ff", "11111111"],


"""
"""
def twoispretty(uwu):
	return "1".join(bin(int(uwu,16))[2:].replace("0", "e").replace("1","0").replace("e", "1").rsplit("0", 1))	
"""
#return rreplace(bin(int(uwu,16))[2:].replace("0", "e").replace("1","0").replace("e", "1"))

"""
def twoc(num):
	return struct.unpack("b", bytes([int(num, 16)]))[0]
"""
"""
def rreplace(s):
	li = s.rsplit("0", 1)
	return "1".join(li)
"""
"""
,
"f":["(non-musical commands)", ]
"""