from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import time
import random as rnd


CORDS = []
distCORDS = []

x0y0z0 = (0,0,0)

CORDS.append(x0y0z0)

R=2

def Distance(x,y,z):
	return np.sqrt(x**2+y**2+z**2)

def AddParticle():
	global CORDS,R
	step = 1
	Theta = rnd.uniform(0,2*np.pi)
	Phi = rnd.uniform(0,2*np.pi)
	x,y,z = int(R*np.sin(Theta)*np.cos(Phi)), int(R*np.sin(Theta)*np.sin(Phi)), int(R*np.cos(Theta))
	while True:
		x,y,z = round(x,2),round(y,2),round(z,2)
		# print(x,y,z)
		s = [
			(x+step,y,z),
			(x-step,y,z),
			(x,y+step,z),
			(x,y-step,z),
			(x,y,z+step),
			(x,y,z-step)
			]
		if Distance(x,y,z) > R+2:#*1.05:
			return
		if len(list(set(s) & set(CORDS))) > 0:
			print(len(CORDS))
			CORDS.append((x,y,z))
			distCORDS.append(Distance(x,y,z))
			R = max(distCORDS)+1
			return
		x += rnd.randint(-1,1)
		y += rnd.randint(-1,1)
		z += rnd.randint(-1,1)
		#print(x,y,z)
		# rand = rnd.randint(1,6)
		# if rand == 1:
		# 	x += step
		# elif rand == 2:
		# 	x += -step
		# elif rand == 3:
		# 	y += step
		# elif rand == 4:
		# 	y += -step
		# elif rand == 5:
		# 	z += step
		# else:
		# 	z += -step
	return

while len(CORDS) <=1000:#True:
	AddParticle()

CordsX = []
CordsY = []
CordsZ = []

for cord in CORDS:
	CordsX.append(cord[0])
	CordsY.append(cord[1])
	CordsZ.append(cord[2])

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.scatter(CordsX,CordsY,CordsZ)

plt.show()