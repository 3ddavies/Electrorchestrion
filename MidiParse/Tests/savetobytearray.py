
fba=[]
with open("C:\\Users\\gabep\\Desktop\\Electrorchestrion\\Midis\\BONEY M.Rasputin K.mid", "rb") as f:
	for line in f:
		for word in line.split():
			fba.append(word)
print(fba)
print(type(fba[0]))
print(fba[0])