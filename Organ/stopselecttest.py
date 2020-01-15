
insdict = {
"test":1,
"reed":3,
"drums":2,


}

def stopselect(tnu):
	atn = ''
	#for tracktitle in tracknames:
	for instrument in insdict:
		if instrument in tnu:
			atn = instrument

	return atn