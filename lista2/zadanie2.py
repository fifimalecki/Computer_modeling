import matplotlib.pyplot as plt
import numpy as np
import random as rnd

direction = [-1,1]
N = 100
Nw = 10000

def wedrowniczek(p):
	position = []
	movement = []
	x = 0
	position.append(x)
	move = rnd.choice(direction)
	x += move
	movement.append(move)
	position.append(x)
	for i in range(0,N-1):
		rand = rnd.randint(1,10)
		if rand <= p:
			move = movement[-1]
			x += move
			movement.append(move)
			position.append(x)
		elif rand > p:
			move = movement[-1]*(-1)
			x += move 
			movement.append(move) 
			position.append(x)
	return position

lastPositions2 = []
lastPositions8 = []

def lastPosition2():
	global lastPositions2
	road = wedrowniczek(2)
	lastPositions2.append(road[-1])
	return road
def lastPosition8():
	global lastPositions8
	road = wedrowniczek(8)
	lastPositions2.append(road[-1])
	return road

xx = np.arange(0,100,1)
roads2 = []
roads8 = []
for i in range(0,Nw):
	road2 = lastPosition2()
	road8 = lastPosition8()
	roads2.append(road2)
	roads8.append(road8)
msdList2 = []
msdList8 = []
for i in range(0,N):
	temp = 0
	for j in range(0,Nw):
		temp += (roads2[j][i]-roads2[j][0])**2
	msdList2.append(temp/Nw)
for i in range(0,N):
	temp = 0
	for j in range(0,Nw):
		temp += (roads8[j][i]-roads8[j][0])**2
	msdList8.append(temp/Nw)
plt.plot(xx,msdList2)
plt.plot(xx,msdList8)
plt.grid()
plt.show()
#jak szybko penetruje w czasie