import numpy as np
import random as rnd
import matplotlib.pyplot as plt
import time

CORDS = []
distCORDS = []

x0y0 = (0,0)

CORDS.append(x0y0)

R=2

def Distance(x,y):
	return np.sqrt(x**2+y**2)

def AddParticle():
	global CORDS,R
	rand = rnd.uniform(0,2*np.pi)
	x,y = int(R*np.cos(rand)), int(R*np.sin(rand))
	while True:
		s = [
			(x+1,y),
			(x,y+1),
			(x-1,y),
			(x,y-1)
			]
		if Distance(x,y) > R+20:
			return
		if len(list(set(s) & set(CORDS))) > 0:
			CORDS.append((x,y))
			distCORDS.append(Distance(x,y))
			R = max(distCORDS)+10
			return
		rand = rnd.randint(1,4)
		if rand == 1:
			x += 1
		elif rand == 2:
			y += 1
		elif rand == 3:
			x += -1
		else:
			y += -1
	return

timein = time.time()
timeout = time.time() + 60*60

while True:
	if time.time() > timeout:
		break
	#print(int(time.time()%60))
	if int(time.time() % 60) == 0:
		print(len(CORDS))
	AddParticle()

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

plt.show()
