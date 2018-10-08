import matplotlib.pyplot as plt
import random as rnd
import numpy as np
import matplotlib.animation as animation

L = 50
p = 0

green = []
red = []
black = []

def MakeGreen(N,p):
	green = []
	for x in range(N):
		for y in range(N):
			rand = rnd.uniform(0,1)
			if rand <= p:
				green.append((x,y))
	return green

green = MakeGreen(L,p)

timeStep = 0

tempRed = []

def FirstStep():
	global green,red,tempRed,timeStep
	for g in green:
		if g[0] == 0:
			tempRed.append(g)
	for r in tempRed:
		green.remove(r)
		red.append(r)
	timeStep += 1

klaster = False

def Step():
	global green,red,black,tempRed,timeStep,klaster
	tempRed = []
	for r in red:
		x = r[0]
		y = r[1]
		s=[(x+1,y),(x,y+1),(x-1,y),(x,y-1),(x+1,y+1),(x-1,y+1),(x+1,y-1),(x-1,y-1)]
		for neighbour in s:
			if neighbour in green:
				if neighbour[0] == L-1:
					klaster = True
				green.remove(neighbour)
				black.append(neighbour)
				tempRed.append(neighbour)
				
	red = tempRed
	timeStep += 1

def Fire():
	time = 1
	FirstStep()
	while len(red) > 0:
		Step()
		time += 1
	return time

# Graph part
averageTimeStep = []
for p in np.arange(0.3,0.6,0.01):
	tav = 0.
	for i in range(100):
		tav += Fire()
		timeStep = 0
		red = []
		black = []
		green = MakeGreen(L,p)
		tempRed = []
	averageTimeStep.append(tav)
	print(p,tav/100)
	#print(f"p={p} klaster={klaster}")

x = np.arange(0.3,0.6,0.01)
fig = plt.figure()
ax = plt.axes(xlim=(-0.1,1.1))
ax.set_xticks(np.arange(0,1.1,0.1))
ax.axis()
ax.grid()
plt.ylabel('Czas')
plt.xlabel('p')
plt.title('L = ' + str(L))
plt.plot(x,averageTimeStep,'b-')
plt.savefig('z1_L'+str(L))

# Animation part

frameG = []
frameR = []
frameB = []


def init():
	fig = plt.figure()
	ax = plt.axes(xlim=(-1,L+1), ylim=(-1,L+1))
	ax.set_xticks(np.arange(0,L,1))
	ax.set_yticks(np.arange(0,L,1))
	ax.set_xticklabels([])
	ax.set_yticklabels([])
	ax.axis()
	ax.grid()

def saveFrames():
	while len(red) > 0:
		init()
		tempG, tempR, tempB = Step()
		frameG.append(tempG)
		frameR.append(tempR)
		frameB.append(tempB)
		plt.plot(*zip(*green),'.',color='green')
		plt.plot(*zip(*red),'o',color='red')
		plt.plot(*zip(*black),'.',color='black')
		plt.savefig(str(len(frameG))+'.png')
		#plt.show()