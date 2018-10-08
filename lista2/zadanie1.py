import matplotlib.pyplot as plt
import numpy as np
import random as rnd

move = [-1,1]
N = 100

def wedrowniczek():
	position = []
	x = 0
	for i in range(0,N):
		x += rnd.choice(move)
		position.append(x)
	return position

pos = []

def lastPosition():
	global pos
	temp = wedrowniczek()
	pos.append(temp[N-1])

y = np.arange(-100,100,1)
for i in range(0,1000):
	lastPosition()

plt.hist(pos,bins=y)
plt.grid()
plt.show()