import numpy as np
import random as rnd
import matplotlib.pyplot as plt
import time

CORDS = []

L=400

x1 = L/2
x2 = -L/2
y1 = L/2
y2 = -L/2

def Distance(x,y):
	return np.sqrt(x**2+y**2)

def AddParticle():
	global CORDS,x1,x2,y1,y2
	x,y = 0,0
	while True:
		s = [ #sprawdzanie sąsiedztwa
			(x+1,y),
			(x,y+1),
			(x-1,y),
			(x,y-1)
			]
		if x == x1 or x == x2 or y == y1 or y == y2:
			print(len(CORDS))
			CORDS.append((x,y))
			return (x,y)
		if len(list(set(s) & set(CORDS))) > 0:
			#print(len(CORDS),(x,y))
			CORDS.append((x,y))
			return (x,y)
		rand = rnd.randint(1,4)
		if rand == 1:
			x += 1
		elif rand == 2:
			y += 1
		elif rand == 3:
			x += -1
		elif rand == 4: 
			y += -1
	return (x,y)

while True:
	last = AddParticle()
	if last == (0,0):
		break

CordsX = []
CordsY = []

for cord in CORDS:
	CordsX.append(cord[0])
	CordsY.append(cord[1])

COLORS = [
		 (1,0,0),
		 (1,127/255,0),
		 (1,1,0),
		 (0,1,0),
		 (102/255,1,1),
		 (102/255,194/255,1),
		 (1,1,1)
		 ]
		 
plt.rcParams['axes.facecolor']='black'
counter = len(CORDS)
for i in range(7):
	plt.plot(CordsX[i*int(counter/7):(i+1)*int(counter/7)],CordsY[i*int(counter/7):(i+1)*int(counter/7)],',',color=COLORS[i])

#plt.plot(CordsX,CordsY,'.',color='red')
plt.show()
