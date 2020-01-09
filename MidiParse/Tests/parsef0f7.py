elif ta[tapc] == "f0" or "f7":#indicates Sysex event
			tapc+=1
			rmc = ta[tapc]#this is the identifier of the meta instruction.
			tapc+=1
			vlvla = True#loop condition
			vlvsa = ''#vlv string
			while vlvla == True:
				vlvsa+=ta[tapc]
				tapc+=1
				if int(ta[tapc], 16) < 128:#indicates that next value will not be  part of the vlv
					vlvla = False
				print(vlvsa)
				print(int(vlvsa,16))
				eventlength = int(vlvsa,16)#this will tell us how many bytes the event is.
			eventraw = []
			for fj in range(0, eventlength):
				eventraw.append(ta[tapc])
				tapc+=1
			event = [edt, rmc, "Sysex Event", [], eventraw]
			print(event)
			print(len(eventraw))
			trackeventsarray.append(event)