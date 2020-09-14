f = open("ppin.txt", "r")
fi=[]
for i in f:
	fi.append(i.replace("\n","").split(";")[3:])
f.close()
#*No;Value;Package;X;Y;Rotation;Side;Name  
#5;;0603-cap;178.217;-85.2938;-90;Top;C12
#['131.729', '-92.033', '180', 'Bottom', 'J269']
g = open("ppout.csv","w")

for j in fi:
	g.write(j[4]+","+j[0]+"mm,"+j[1]+"mm,"+j[3]+","+j[2].replace("-90","270")+"\n")
g.close()