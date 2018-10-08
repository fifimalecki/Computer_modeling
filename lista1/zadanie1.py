import numpy as np
import random as rnd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def distance(*args):
	tempSquareCords = []
	for arg in args:
		tempSquareCords.append(arg**2)
	return np.sqrt(sum(tempSquareCords))

a = 2
N = 10**6
Nk = 0

listOfPointsX = []
listOfPointsY = []
listOfPointsZ = []

listOfPointsXCircle = []
listOfPointsYCircle = []
listOfPointsZCircle = []

for i in range(0,N+1):
	x = rnd.uniform(-1,1)
	y = rnd.uniform(-1,1)
	z = rnd.uniform(-1,1)
	if distance(x,y,z) <= 1:
		listOfPointsXCircle.append(x)
		listOfPointsYCircle.append(y)
		listOfPointsZCircle.append(z)
		Nk += 1
	else:
		listOfPointsX.append(x)
		listOfPointsY.append(y)
		listOfPointsZ.append(z)
Pk = (a**3)*(Nk/N)
print("Objetnosc kola = ",Pk,4/3*np.pi)

# fig = plt.figure()

# ax = fig.add_subplot(111,projection='3d')
# for i in range(0,len(listOfPointsXCircle)):
# 	ax.scatter(listOfPointsXCircle[i],listOfPointsYCircle[i],listOfPointsZCircle[i],',',color='blue')
# plt.show()