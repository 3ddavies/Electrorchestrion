from binascii import unhexlify
from mididictionaries import *
import argparse
verbpa = argparse.ArgumentParser()
verbpa.add_argument('-v', '--verbose', action="store_true", help="enables verbose output (debug)")
vera = verbpa.parse_args()
if vera.verbose:
	def verpri(stuff):
		print(stuff)
else:
	def verpri(stuff):
		pass

#<MTrk event> = <delta-time> <event>
#for meta dt00ffblahblahblah
def keysig(ks):
	pass

y = '00ff7f0d050f1c323030332e31322e303100ff7f08050f1200007f7f0000ff5103068a1a00ff58040402180800ff2f00'
z="00ff03095361786f70686f6e658c00c44100b4076401b45b2801943a57827e943e5702843a57827e843e5700944157830084415700944557830084455700944357830084435700944157830084415700943e578300843e5700943a578300843a5700943c578300843c5700943f578300843f57009443578300844357009446578300844657009445578b5c84455724943a578300843a5700943e578300843e5700944157830084415700944557830084455700944357830084435700944157830084415700943e578300843e5700943a578300843a5700943c578300843c5700943f578300843f5700944357830084435700944657830084465700944557856e844557838012944166825084416630944366825084436630944566825084456630944366884c8443668c34944566825084456630944566825084456630944366825084436630944566884c844566893494466682508446663094466682508446663094456682508445663094466682508446663094466682508446668330944566825084456630943f668250843f6630943f668250843f6630943e668250843e6630943f668550843f668c3094456682508445663094456682508445663094436682508443663094456682508445668630944366825084436630943e668250843e6630943e668250843e6630943c668250843c6630943e668550843e663094416682508441668930944866825084486630944866825084486630944666825084466630944866825084486630944666825084466630944866825084486630944666825084466630944966852084496660944966852084496660944a668250844a663094486682508448668630944566825084456630944366856e8443668f1294456682508445663094456682508445663094436682508443663094456685508445668c3094466682508446663094466682508446663094456682508445663094466682508446663094466682508446668330944566825084456630943f668250843f668330943e668250843e6630943f668550843f668930943c668520843c6660943f668250843f6630944366855084436630944666825084466630944666825084466630944666825084466630944866912084486660944666825084466630944866825084486630944a668520844a6660944a668520844a6660944a668250844a6630944666825084466630944a668250844a66309446668d408446669340944161830084416100944361830084436100944561825084456130944361884c8443618f34944961830084496100944561830084456100944061830084406100943e61884c843e619b34944764830084476400944664830084466400944564830084456400944464830084446400944364884c8443648334944561825084456130944861830084486100944561830084456100944361825084436130944161830084416100944161830084416100944161830084416100944161856e84416112943c64884c843c648334944861825084486130944861825084486130944661825084466130944861825084486130944661825084466130944861825084486130944661825084466130944961852084496160944961852084496160944a618250844a6130944861825084486130944561830084456100944161825e84416122943e61884c843e618334944561825084456130944361856e8443618f12944561825084456130944561825084456130944361825084436130944561825e84456122943e61884c843e619b34944361830084436100944161830084416100943f618300843f6100943e618300843e6100943c618520843c6160943f618250843f6130944361855084436130944661825084466130944661825084466130944661825084466130944861912084486160944666825084466630944866825084486630944a668520844a6660944a668520844a6660944a668250844a6630944666825084466630944a668250844a66309446668d4084466600ff2f00"
x="00ff20010000ff0307547261636b203800ff0309326e6420566f696365e60090417f825080417f3090437f825080437f3090417f825080417f3090417f884c80417f8c3490407f825080407f3090407f825080407f3090407f825080407f3090407f884c80407f893490427f825080427f3090427f825080427f3090427f825080427f3090427f825080427f3090427f825080427f833090427f825080427f30903b7f8250803b7f30903b7f8250803b7f30903b7f8250803b7f30903b7f8550803b7f8c3090407f825080407f3090407f825080407f3090407f825080407f3090407f825080407f863090407f825080407f3090397f825080397f3090397f825080397f3090397f825080397f3090397f855080397f30903c7f8250803c7f893090457f825080457f3090457f825080457f3090437f825080437f3090457f825080457f3090437f825080437f3090457f825080457f3090437f825080437f3090447f852080447f6090447f852080447f6090457f825080457f3090457f825080457f863090417f825080417f3090417f856e80417f8f1290407f825080407f3090407f825080407f3090407f825080407f3090407f855080407f8c3090427f825080427f3090427f825080427f3090427f825080427f3090427f825080427f3090427f825080427f833090427f825080427f30903b7f8250803b7f8330903b7f8250803b7f30903b7f8550803b7f893090377f852080377f60903c7f8250803c7f30903f7f8550803f7f3090437f825080437f3090437f825080437f3090437f825080437f3090427f912080427f6090427f825080427f3090427f825080427f3090467f852080467f6090467f852080467f6090467f825080467f3090437f825080437f3090467f825080467f3090417f8d4080417f83874090417f825080417f3090437f825080437f3090417f825080417f3090417f884c80417f8c3490407f825080407f3090407f825080407f3090407f825080407f3090407f884c80407f893490427f825080427f3090427f825080427f3090427f825080427f3090427f825080427f3090427f825080427f833090427f825080427f30903b7f8250803b7f30903b7f8250803b7f30903b7f8250803b7f30903b7f8550803b7f8c3090407f825080407f3090407f825080407f3090407f825080407f3090407f825080407f863090407f825080407f3090397f825080397f3090397f825080397f3090397f825080397f3090397f855080397f30903c7f8250803c7f893090457f825080457f3090457f825080457f3090437f825080437f3090457f825080457f3090437f825080437f3090457f825080457f3090437f825080437f3090447f852080447f6090447f852080447f6090457f825080457f3090457f825080457f863090417f825080417f3090417f856e80417f8f1290407f825080407f3090407f825080407f3090407f825080407f3090407f855080407f8c3090427f825080427f3090427f825080427f3090427f825080427f3090427f825080427f3090427f825080427f833090427f825080427f30903b7f8250803b7f8330903b7f8250803b7f30903b7f8550803b7f893090377f852080377f60903c7f8250803c7f30903f7f8550803f7f3090437f825080437f3090437f825080437f3090437f825080437f3090427f912080427f6090427f825080427f3090427f825080427f3090467f852080467f6090467f852080467f6090467f825080467f3090437f825080437f3090467f825080467f3090417f8d4080417f00ff2f00"
w='00ff03075472756d7065748c00b35b2800c33800b307640193353e827f933a3e0183353e827f833a3e00933e3e8300833e3e0093413e830083413e00933a3e8b5c833a3e2493393e830083393e00933c3e8300833c3e00933f3e8300833f3e0093433e830083433e0093413e8b5c83413e2493353e830083353e00933a3e8300833a3e00933e3e8300833e3e0093413e830083413e00933a3e8b5c833a3e2493393e830083393e00933c3e8300833c3e00933f3e8300833f3e0093433e830083433e0093413e856e83413e83801293414a825083414a3093434a825083434a3093414a825083414a3093414a884c83414a8c3493404a825083404a3093404a825083404a3093404a825083404a3093404a884c83404a893493424a825083424a3093424a825083424a3093424a825083424a3093424a825083424a3093424a825083424a833093424a825083424a30933b4a8250833b4a30933b4a8250833b4a30933b4a8250833b4a30933b4a8550833b4a8c3093404a825083404a3093404a825083404a3093404a825083404a3093404a825083404a8630933e4a8250833e4a3093394a825083394a3093394a825083394a3093394a825083394a3093394a855083394a30933c4a8250833c4a893093454a825083454a3093454a825083454a3093434a825083434a3093454a825083454a3093434a825083434a3093454a825083454a3093434a825083434a3093444a852083444a6093444a852083444a6093454a825083454a3093454a825083454a863093414a825083414a3093414a856e83414a8f1293404a825083404a3093404a825083404a3093404a825083404a3093404a855083404a8c3093424a825083424a3093424a825083424a3093424a825083424a3093424a825083424a3093424a825083424a833093424a825083424a30933b4a8250833b4a8330933b4a8250833b4a30933b4a8550833b4a893093374a852083374a60933c4a8250833c4a30933f4a8550833f4a3093434a825083434a3093434a825083434a3093434a825083434a3093424a912083424a6093424a825083424a3093424a825083424a3093464a852083464a6093464a852083464a6093464a825083464a3093434a825083434a3093464a825083464a3093414a8d4083414a00ff2f00'
#the output is an array containing arrays for each event. The final array will be several of the following:
#[deltatime, eventID, eventname, [arbitrary bytes in hex], [bytes in hex of event.]]
def mparse(stringcheese):
	ta = [(stringcheese[i:i+2]) for i in range(0, len(stringcheese), 2)]#splits the track string into an array of bytes.
	tapc = 0#pos counter
	trackeventsarray = []#stores all events in a track.
	while len(ta) > tapc:
		verpri('tapc '+str(tapc))
		dtl = True#loop condition
		edt = ''#event delta time
		while dtl == True:
			edt+=ta[tapc]
			if int(ta[tapc], 16) < 128:#indicates that next value will not be  part of the vlv
				dtl = False
			tapc+=1
		arb = []
		if ta[tapc] == "ff":#indicates MIDI meta event
			tapc+=1
			rmc = ta[tapc]#this is the identifier of the meta instruction.
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
			if midimeta[rmc][3] == True:
				event.append(unhexlify("".join(eventraw)).decode())
			verpri(event)
			verpri(len(eventraw))
			trackeventsarray.append(event)
		elif ta[tapc] == "f0":#indicates f0 sysex event
			verpri("f0 sysex event")

		elif ta[tapc] == "f7":#indicates f7 sysex event
			verpri("f7 sysex event")

		elif ta[tapc][0] in musicalevents:#if the event is a musical event:
			ev= ta[tapc]#event. ev[0] will be the event name while ev[1] is the channel.
			tapc+=1
			verpri('Event "' + musicalevents[ev[0]][0] + '" on channel ' + str(ev[1]))
			evdata = ta[tapc:tapc+musicalevents[ev[0]][1]]
			tapc+=musicalevents[ev[0]][1]
			verpri(evdata)
			event = [edt, ev, 'Event "' + musicalevents[ev[0]][0] + '" on channel ' + str(ev[1]), [], evdata]
			trackeventsarray.append(event)

		else:
			print("stuck!", ta[tapc])
			exit()
	return trackeventsarray
print(mparse(w))