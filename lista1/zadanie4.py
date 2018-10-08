import numpy as np 
import random as rnd

N = 10**3
success = 0
deck = list(np.arange(1,101,1))

for j in range(0,N):
	counter = 0
	for i in range(0,len(deck)):
		rnd.shuffle(deck)
		if deck[i] == i+1:
			counter += 1
	success += counter

print(success/N)