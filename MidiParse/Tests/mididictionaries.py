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