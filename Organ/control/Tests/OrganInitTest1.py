import os

wkdr = os.getcwd().split("Organ\\control\\Tests")[0]#the root directory of the repo.
#print(wkdr)

orgar=[]#2d array. in format of ["manufacturer", [opus, opus]]
ops=[]#2darray of opuses
obsrc = 0#recursion counter
for obs in os.walk(wkdr+"\\Organ\\config"):
	if obsrc == 0:
		manuf=obs[1]#manufacturers
	else:
		ops.append(obs[2])
	obsrc+=1
print(manuf)
print(ops)