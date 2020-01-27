from organdicts import *

insdict = {
"test":1,
"reed":3,
"drums":2,


}

exa = [['53', 'Voice Oohs', 'd'], ['26', 'Electric Guitar (jazz)', 'e'], ['65', 'Alto Sax', '4'], ['56', 'Trumpet', '3'], ['35', 'Fretless Bass', '1']]

def stopselect(tnu):
		
	for patches in tnu:#foreachtrack
		if patches[1] in organstops:	
			print(True)


stopselect(exa)
"""
	atn = ''
	#for tracktitle in tracknames:
	for instrument in insdict:
		if instrument in tnu:
			atn = instrument

	return atn
"""