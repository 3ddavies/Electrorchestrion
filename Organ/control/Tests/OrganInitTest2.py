import os
import configparser

config = configparser.ConfigParser()

global wkdr
wkdr = os.getcwd().split("Organ\\control\\Tests")[0]#the root directory of the repo.

def lsogns():#lists organs
	global wkdr
	orgar=[]#2d array. in format of ["manufacturer", [opus, opus]]
	obsrc = 0#recursion counter
	orgtry = True
	sctry = True
	for obs in os.walk(wkdr+"\\Organ\\config"):
		if obsrc == 0:
			for manu in obs[1]:#for each manufacturer
				orgar.append([manu])
		else:
			orgar[obsrc-1].append(obs[2])#appends opuses
		obsrc+=1
	for brnds in range(0,len(orgar)):
		print(str(brnds) +"-"+orgar[brnds][0])
		for sns in range(0,len(orgar[brnds][1])):#for opus
			print("	"+str(sns)+"-"+os.path.splitext(orgar[brnds][1][sns])[0])
	print("please select which organ you would like to use. Format: manufacturer,organ")
	while orgtry == True:
		try:
			sel = input("->").split(",")
			print(orgar[int(sel[0])][1][int(sel[1])])
			orgtry = False
		except ValueError:
			print("Invalid input. Please input your selection in the format: manufacturer,organ")
		except IndexError:
			print("Invalid input. You have made a selection out of the available range. Please input your selection in the format: manufacturer,organ")
	print("Would you like to make '"+str(orgar[int(sel[0])][0])+": "+os.path.splitext(orgar[int(sel[0])][1][int(sel[1])])[0]+"' the default configuration? Y/N")
	while sctry == True:
		sc=input("->").upper()
		if sc == "Y":
			config['DEFAULT']['path'] = str(orgar[int(sel[0])][0])+"\\"+str(orgar[int(sel[0])][1][int(sel[1])])
			config['DEFAULT']['manufacturer'] = str(orgar[int(sel[0])][0])
			config['DEFAULT']['organ'] = os.path.splitext(orgar[int(sel[0])][1][int(sel[1])])[0]
			config.write(open(wkdr+'\\Organ\\config\\config.ini', 'w'))
			sctry = False
		elif sc == "N":
			sctry = False
		else:
			print("Invalid input. Format: Y/N")

try:
	config.read(wkdr+'\\Organ\\config\\config.ini')
	otu = config['DEFAULT']['path']
	#print(wkdr+"\\"+otu)
	print("Loading configuration for '"+config['DEFAULT']['manufacturer']+": "+config['DEFAULT']['organ']+"'")
except:
	lsogns()