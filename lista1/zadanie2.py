import numpy as np
import random as rnd
from scipy import integrate
import scipy

def distance(*args):
	tempSquareCords = []
	for arg in args:
		tempSquareCords.append(arg**2)
	return sum(tempSquareCords)**(1/2)

def C(n):
	return np.pi**(n/2)/(scipy.special.gamma(n/2+1))

def volumeOfNSphere(r,n):
	return C(n)*(r**n)

dimension = 15
a = 2
N = 10**6

#while dimension <= 15:
Nk = 0
listOfPoints = []
listOfPointsHiperball = []


for i in range(0,N+1):
	cords = []
	for i in range(0,dimension):
		cord = rnd.uniform(-1,1)
		cords.append(cord)
	if distance(*cords) <= 1:
		Nk += 1

Pk = (a**dimension)*(Nk/N)
resultFromEquation = volumeOfNSphere(1,dimension)
print("\nWymiar : ",dimension,"\nObjetnosc kola (Monte Carlo)= ",Pk,"\nObjetosc kola (wzor) = ",resultFromEquation,"\nBlad = ",abs(Pk-resultFromEquation),"Nk=",Nk)
dimension +=1