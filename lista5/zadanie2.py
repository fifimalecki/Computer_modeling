import matplotlib.pyplot as plt
import random as rnd
import numpy as np

L = 50

green = np.zeros((L,L))
red = []
#green[y][x]


def MakeGreen(N,p):
	global green
	for y in range(N):
		for x in range(N):
			rand = rnd.uniform(0,1)
			if rand <= p:
				green[x][y] = -1
			else:
				green[x][y] = 1


def FirstStep():
	global green,red
	tempRed = []
	for y in range(L):
		if green[y][0] < 0:
			tempRed.append((y,0))
			green[y][0] = 0
	red = tempRed

def Step():
	global green,red,klaster
	tempRed = []
	for r in red:
		x = r[1]
		y = r[0]
		s=[(x+1,y),(x,y+1),(x-1,y),(x,y-1),(x+1,y+1),(x-1,y+1),(x+1,y-1),(x-1,y-1)]
		for neighbour in s:
			if  neighbour[1] >= 0 and neighbour[1] < L and neighbour[0] >= 0 and neighbour[0] < L and green[neighbour[1]][neighbour[0]] < 0:
				if neighbour[0] == L-1:
					klaster = True
				green[neighbour[1]][neighbour[0]] = 0
				tempRed.append((neighbour[1],neighbour[0]))
	red = tempRed



def Fire():
	time = 1
	FirstStep()
	while len(red) > 0:
		Step()
		time += 1
	return time

MakeGreen(L,0)
klaster = False	
klastry = 0
averageTimeStep = []
klasterList = []

min, max, step = 0.0,1,0.01

result = 0.0

M = 100

x = np.arange(min,max,step)

for p in np.arange(min,max,step):
	tav = 0.0
	klastry = 0
	for i in range(M):
		tav += Fire()
		if(klaster == True):
			klastry += 1
		MakeGreen(L,round(p,2))
		red = []
		klaster = False
	averageTimeStep.append(tav/M)
	klasterList.append(klastry/M)
	print(p,tav/M,klastry/M)

print(sum(klasterList)/len(klasterList))

fig = plt.figure()
ax = plt.axes(xlim=(min-step,max+step))
ax.set_xticks(np.arange(min,max,step))
ax.axis()
ax.grid()
plt.ylabel('Czas')
plt.xlabel('p')
plt.title('L = ' + str(L))
plt.plot(x,averageTimeStep,'b-')
# plt.savefig('z1_L'+str(L))
plt.show()