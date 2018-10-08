import numpy as np
import matplotlib.pyplot as plt
import random as rnd
import turtle

N = 100
Nw = 1000

def wedrowniczek(length):
	x0, y0 = 0,0
	x,y = x0,y0
	walkx,walky = [x],[y]
	for i in range(length):
		rand = rnd.randint(1,4)
		if rand == 1:
			x += 1
		elif rand == 2:
			y += 1
		elif rand == 3:
			x += -1
		elif rand == 4: 
			y += -1
		walkx.append(x)
		walky.append(y)
	return [walkx,walky]

lastPositions = []

for i in range(Nw):
	walk  = wedrowniczek(N)
	lastPositions.append([walk[0][-1],walk[1][-1]])
	plt.plot(walk[0],walk[1])
lastPositionInStart = 0
for lastPos in lastPositions:
	if lastPos[0] == 0 and lastPos[-1] == 0:
		lastPositionInStart += 1
print(lastPositionInStart)
plt.axis([-30,30,-30,30])
plt.grid()
plt.show()
