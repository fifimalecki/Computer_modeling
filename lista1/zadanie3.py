import numpy as np 
import random as rnd

def func(x):
	return (1/np.sqrt(2*np.pi))*np.exp(-(x**2)/2)

N = 1
for i in range(0,3):
	N *= 100
	listOfY = []

	for i in range(0,N):
		x = rnd.uniform(-2,2)
		y = func(x)
		listOfY.append(y)

	result = sum(listOfY)/len(listOfY)

	print("N=",N,"Wynik=",result*4)