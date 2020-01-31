from math import *
#by default I will only use the first 24 pins, meaning 8 rows of 8, or 64 built in registers.
#512 outputs
#233
"""

x = [[1,2,3,4,5,6,7,8], [1,2,3,4,5,6,7,8], [1,2,3,4,5,6,7,8], [1,2,3,4,5,6,7,8], [1,2,3,4,5,6,7,8], [1,2,3,4,5,6,7,8], [1,2,3,4,5,6,7,8], [1,2,3,4,5,6,7,8]]
64+64+64
"""

#actualPin = pin - (8 * reg);
global numofregisters
numofregisters = 64
def regnum(pinnum):
	global numofregisters
	registernum = ceil(pinnum/8)#the register number the pin will be on.
	rrn = ceil(registernum/(ceil(numofregisters/8)))#row number
	rinr = registernum-(registernum// 8)*8#register num in the row. eg register 3 in row 4.
	rpn = pinnum-(pinnum// 8)*8#pin num on the register.
	print("Pin " + str(pinnum) + " is on register " + str(registernum) + ". Pin " + str(rpn) + " register " + str(rinr) + " on row " + str(rrn))