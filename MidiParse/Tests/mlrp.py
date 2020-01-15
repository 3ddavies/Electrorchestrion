f = open("mlr.txt", "r")
x = f.read()
y=x.split("\n")
z = []
a = []

for i in y:
	z.append(i.split(". "))

for j in z:
	j[0] = str(int(j[0])-1)

for k in z:
	#a.append(str(k[0]) + ". " + str(k[1]))
	print('"' + str(k[0]) + '": "' + str(k[1]) + '",')
print("}")
#print(a)
#print(type(a))