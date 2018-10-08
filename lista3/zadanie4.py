import numpy as np
import matplotlib.pyplot as plt
import random as rnd

h = 100

p1 = 0.6
p2 = 0.1 + p1
p3 = 0.15 + p2
p4 = 0.15 + p3

N = 10
Nw = 1000 

def RainDrop():
	x0, y0 = 0,h
	x,y = x0,y0
	walkx,walky = [x],[y]
	t = 0
	while y >= 0:
		rand = rnd.randint(1,100)/100
		if rand <= p1:
			y += -1
		elif rand > p1 and rand <= p2:
			y += 1
		elif rand > p2 and rand <= p3:
			x += 1
		elif rand > p3 and rand <= p4: 
			x += -1
		else:
			x += 0
			y += 0
		t += 1
		walkx.append(x)
		walky.append(y)
	return [walkx,walky], t

tList = []
msdList = []
roads = []

for i in range(N):
	hRoadsList = []
	for j in range(Nw):
		walk,T = RainDrop()
		tList.append(T)
		hRoadsList.append(walk)
	roads.append(hRoadsList)
	h+=100

#roads[wysokosc][index na wysokosci][x/y]

for i in range(N):
	temp = 0
	avgMsdList = []
	for j in range(Nw):
		temp = 0
		for k in roads[i][j][0]:
			temp += (k-roads[i][j][0][0])**2
		avgMsdList.append(temp/Nw)
	msdList.append(sum(avgMsdList)/len(avgMsdList))
	print(sum(avgMsdList)/len(avgMsdList))

# print(tList)
plt.plot(np.arange(100,1100,100),msdList,'.--')
plt.grid()
plt.show()