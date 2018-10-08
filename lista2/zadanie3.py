import matplotlib.pyplot as plt
import numpy as np
import random as rnd

direction = [-1,1]
N = 100
Nw = 10000
a = 5
absorbingNode1 = 0
absorbingNode2 = 2*a
x0 = 0


def wedrowniczek(p):
	position = []
	movement = []
	steps = 0
	x = x0
	position.append(x)
	if x0 == absorbingNode1 or x0 == absorbingNode2:
		return steps, position
	move = rnd.choice(direction)
	x += move
	steps += 1
	movement.append(move)
	position.append(x)
	while(x > absorbingNode1 or x < absorbingNode2):
		rand = rnd.randint(1,10)
		if x == absorbingNode1 or x == absorbingNode2:
			return steps, position
		if rand <= p:
			move = movement[-1]
			x += move
			steps +=1
			movement.append(move)
			position.append(x)
		elif rand > p:
			move = movement[-1]*(-1)
			x += move 
			steps += 1
			movement.append(move)
			position.append(x)
	return steps, position

AveregesT = []

while x0 <= 10:
	averageT = 0
	for i in range(Nw):
		steps, position = wedrowniczek(5)
		#plt.plot(np.arange(0,steps+1,1),position)
		averageT += steps
	AveregesT.append(averageT/Nw)
	print(averageT/Nw)
	x0 += 1

plt.plot(np.arange(0,11,1),AveregesT)
plt.plot(np.arange(0,11,1),AveregesT,'.')

plt.grid()
plt.show()