f = open("test.txt", 'r')
s="4d546864000000060001000201804d54726b0000003000ff7f0d050f1c323030332e31322e303100ff7f08050f1200007f7f0000ff5103068a1a00ff58040402180800ff2f004d54726b00000516"
s+= f.read()
s = "\n".join(s[i:i+16] for i in range(0, len(s), 16))
f.close()
g = open("p2.txt", 'w+')
g.write(s)
g.close()



gabe = len(open("p2.txt", "r").readlines())
j=open("p2.txt", "r")


ggg = ''
for i in range(0, gabe):
	idk = j.readline()
	wdk = " ".join(idk[i:i+2] for i in range(0, len(idk), 2))
	ggg += wdk[:len(wdk)]
j.close()
m = open("track.mid", 'wb+')
m.write(ggg.encode())
m.close()

'''
ggg = ''
n = open("track.txt", "r")
gabew = len(open("track.txt", "r").readlines())
for i in range(0, gabe):
	idk = n.readline()
	idk = idk[:len(idk)-1]
	ggg += idk
print(ggg)
'''