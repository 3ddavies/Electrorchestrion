
def mparse(stringcheese):
	ta = [(stringcheese[i:i+2]) for i in range(0, len(stringcheese), 2)]#splits the track string into an array of bytes.
	tapc = 0#pos counter
	trackeventsarray = []#stores all events in a track.
	trackins=[]#instruments
	tchn = ''

	while len(ta) > tapc:
		verpri('tapc '+str(tapc))
		dtl = True#loop condition
		edt = ''#event delta time
		while dtl == True:
			edt+=ta[tapc]
			if int(ta[tapc], 16) < 128:#indicates that next value will not be  part of the vlv
				dtl = False
			tapc+=1
			verpri("edt " +str(edt))
		arb = []
		if ta[tapc] == "ff":#indicates MIDI meta event
			tapc+=1
			rmc = ta[tapc]#this is the identifier of the meta instruction.
			verpri("RMC: "+str(rmc))
			tapc+=1
			if midimeta[rmc][2] == 'vlv':
				verpri(True)
				vlvl = True#loop condition
				vlvs = ''#vlv string
				while vlvl == True:
					vlvs+=ta[tapc]
					tapc+=1
					if int(ta[tapc], 16) < 128:#indicates that next value will not be  part of the vlv
						vlvl = False
				verpri(vlvs)
				verpri(int(vlvs,16))
				eventlength = int(vlvs,16)#this will tell us how many bytes the event is.
			else:
				for k in range(0,midimeta[rmc][1]):
					arb.append(ta[tapc])
					tapc+=1
				eventlength = midimeta[rmc][2]
			eventraw = []
			for j in range(0, eventlength):
				eventraw.append(ta[tapc])
				tapc+=1
			event = [edt, rmc, midimeta[rmc][0], arb, eventraw]
			if midimeta[rmc][3] == True:#if the event is a text event, append a string with the decoded ASCII to the array.
				event.append(unhexlify("".join(eventraw)).decode())
			elif rmc == "59":#if the event is a keysig event
				event.append(keysig(eventraw[0]))

			if rmc == "03":
				print("03 gabe ", event)
				tchn = event[len(event)-1]

			verpri(event)
			verpri(len(eventraw))
			trackeventsarray.append(event)

		elif ta[tapc][0] in musicalevents:#if the event is a musical event:
			rmc= ta[tapc]#event. rmc[0] will be the event name while rmc[1] is the channel.
			tapc+=1
			verpri("RMC: "+str(rmc))
			verpri('Event "' + musicalevents[rmc[0]][0] + '" on channel ' + str(rmc[1]))
			evdata = ta[tapc:tapc+musicalevents[rmc[0]][1]]
			tapc+=musicalevents[rmc[0]][1]
			event = [edt, rmc, 'Event "' + musicalevents[rmc[0]][0] + '" on channel ' + str(rmc[1]), [], evdata]
			verpri(event)
			trackeventsarray.append(event)
			if rmc[0] == "c":#patch change
					trackins.append([str(int(event[len(event)-1][0], 16)), midiprogs[str(int(event[len(event)-1][0], 16))],  str(rmc[1])])

		elif ta[tapc] in ["f0", "f7"]:#indicates Sysex event
			rmc = ta[tapc]#this is the identifier of the meta instruction.
			tapc+=1
			vlvla = True#loop condition
			vlvsa = ''#vlv string
			while vlvla == True:
				vlvsa+=ta[tapc]
				tapc+=1
				if int(ta[tapc], 16) < 128:#indicates that next value will not be  part of the vlv
					vlvla = False
				verpri(vlvsa)
				verpri(int(vlvsa,16))
			eventlength = int(vlvsa,16)#this will tell us how many bytes the event is.
			eventraw = []
			for fj in range(0, eventlength):
				eventraw.append(ta[tapc])
				tapc+=1
			event = [edt, rmc, "Sysex Event", [], eventraw]
			verpri(event)
			verpri(len(eventraw))
			trackeventsarray.append(event)
			#tapc+=1





		else:#if there is no event code, we can assume that it is the same as the previous event's code.
			if rmc in midimeta:
				if midimeta[rmc][2] == 'vlv':
					verpri(True)
					vlvl = True#loop condition
					vlvs = ''#vlv string
					while vlvl == True:
						vlvs+=ta[tapc]
						tapc+=1
						if int(ta[tapc], 16) < 128:#indicates that next value will not be  part of the vlv
							vlvl = False
					verpri(vlvs)
					verpri("event length", int(vlvs,16))
					verpri("event length", vlvs)
					eventlength = int(vlvs,16)#this will tell us how many bytes the event is.
				else:
					for lll in range(0,midimeta[rmc][1]):
						arb.append(ta[tapc])
						tapc+=1
					eventlength = midimeta[rmc][2]
				eventraw = []
				for jjj in range(0, eventlength):
					eventraw.append(ta[tapc])
					tapc+=1
				event = [edt, rmc, midimeta[rmc][0], arb, eventraw]
				if midimeta[rmc][3] == True:#if the event is a text event, append a string with the decoded ASCII to the array.
					try:
						event.append(unhexlify("".join(eventraw)).decode())
					except:
						#verpri(eventraw)
						verpri(event)
						exit()
				elif rmc == "59":#if the event is a keysig event
					event.append(keysig(eventraw[0]))
				verpri(event)
				verpri(len(eventraw))
				trackeventsarray.append(event)
				verpri("SPECIAL EVENT")
				#exit()

			elif rmc[0] in musicalevents:
				verpri('Event "' + musicalevents[rmc[0]][0] + '" on channel ' + str(rmc[1]))
				evdata = ta[tapc:tapc+musicalevents[rmc[0]][1]]
				tapc+=musicalevents[rmc[0]][1]
				event = [edt, rmc, 'Event "' + musicalevents[rmc[0]][0] + '" on channel ' + str(rmc[1]), [], evdata]
				verpri(event)
				trackeventsarray.append(event)
				verpri("SPECIAL EVENT")
				#exit()
				if rmc[0] == "c":#patch change
					trackins.append(midiprogs[str(int(event[len(event)-1][0], 16))])


			else:
				print("stuck!", ta[tapc])
				print("EDT ", edt)
				print(rmc)
				#exit()

	return trackeventsarray, trackins, tchn