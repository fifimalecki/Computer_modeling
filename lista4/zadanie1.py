import numpy as np
import random as rnd
import matplotlib.pyplot as plt

CORDS = []
avaibleNodes = []
border = 30

x0y0 = [0,0]

CORDS.append(x0y0)

avaibleNodes.append([x0y0[0]+1,x0y0[1]])
avaibleNodes.append([x0y0[0],x0y0[1]+1])
avaibleNodes.append([x0y0[0]-1,x0y0[1]])
avaibleNodes.append([x0y0[0],x0y0[1]-1])

def AddMass():
	global CORDS, avaibleNodes
	tempCords = []
	NavaibleNodes = len(avaibleNodes)
	rand = rnd.randint(0,NavaibleNodes-1)
	tempCords = avaibleNodes[rand]
	CORDS.append(tempCords)
	avaibleNodes.remove(tempCords)
	newNodes = []
	UpdateANodes(tempCords)
	for node in avaibleNodes:
		if node in CORDS:
			avaibleNodes.remove(node)

def UpdateANodes(point):
	global avaibleNodes, CORDS
	newNodes = []
	newNodes.append([point[0]+1,point[1]])
	newNodes.append([point[0],point[1]+1])
	newNodes.append([point[0]-1,point[1]])
	newNodes.append([point[0],point[1]-1])
	for newNode in newNodes:
		if newNode in CORDS:
			newNodes.remove(newNode)
	for newNode in newNodes:
		if newNode in avaibleNodes:
			newNodes.remove(newNode)
	for newNode in newNodes:
		avaibleNodes.append(newNode)

counter = 0

while True:
	counter +=1
	AddMass()
	if CORDS[-1][0] >= border or CORDS[-1][1] >= border or CORDS[-1][0] <= -border or CORDS[-1][1] <= -border:
		break

CordsX = []
CordsY = []

aNodesX = []
aNodesY = []

for cord in CORDS:
	CordsX.append(cord[0])
	CordsY.append(cord[1])


for node in avaibleNodes:
	aNodesX.append(node[0])
	aNodesY.append(node[1])

COLORS = [
		 (1,0,0),
		 (1,127/255,0),
		 (1,1,0),
		 (0,1,0),
		 (0,0,1),
		 (75/255,0,130/255),
		 (148/255,0,211/255)
		 ]
		 
plt.rcParams['axes.facecolor']='black'
for i in range(7):
	plt.plot(CordsX[i*int(counter/7):(i+1)*int(counter/7)],CordsY[i*int(counter/7):(i+1)*int(counter/7)],'.',color=COLORS[i])
plt.plot(aNodesX,aNodesY,'.',color='white')
plt.show()