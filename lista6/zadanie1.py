import matplotlib.pyplot as plt
import random as rnd
import numpy as np

x0 = rnd.uniform(0,1)
print(x0)
rList = [0.2,0.5,0.8,0.88,0.92,0.96,1.0]
k =4.0

def xn1(r,xn):
	return k * r * xn * (1 - xn)

n = np.arange(0,100,1)

for r in rList:
	XnList = []

	tempXn = xn1(r,x0)
	XnList.append(tempXn)

	for i in range(99):
		tempXn = xn1(r,tempXn)
		XnList.append(tempXn)

	#plt.title('r='+str(r))
	plt.plot(n,XnList,label='r='+str(r))
	plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.)
plt.show()