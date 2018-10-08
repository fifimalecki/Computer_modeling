import random as rnd
import matplotlib.pyplot as plt

class Percolation_NZ:
	L = 64			# Linear dimension
	N = L*L 		# Total dimension
	EMPTY = -N-1	# Empty site label

	ptr = []		# Array of pointer
	nn = []			# Nearest neighbors
	order = []		# Occupation order

	Big = []

	def __init__(self):
		self.ptr = [None] * self.N
		for i in range(self.N):
			temp = [None] * 4
			self.nn.append(temp)
		self.order = [None] * self.N
		self.Big = [None] * self.N
		self.Big[0] = 0

	def boundaries(self):
		for i in range(self.N):
			self.nn[i][0] = (i+1)%self.N
			self.nn[i][1] = (i+self.N-1)%self.N
			self.nn[i][2] = (i+self.L)%self.N
			self.nn[i][3] = (i+self.N-self.L)%self.N
			if i%self.L == 0:
				self.nn[i][1] = i+self.L-1
			if (i+1)%self.L == 0:
				self.nn[i][0] = i-self.L+1

	def permutation(self):
		temp = 0

		for i in range(self.N):
			self.order[i] = i
		for i in range(self.N):
			rand = rnd.randint(0,self.N-i-1)
			j = i + rand
			temp = self.order[i]
			self.order[i] = self.order[j]
			self.order[j] = temp

	def findroot(self,i):
		if self.ptr[i]<0:
			return i
		return self.findroot(self.ptr[i])

	def percolate(self):
		i,j = 0,0
		s1,s2 = 0,0
		r1,r2 = 0,0
		big = 0

		for i in range(self.N):
			self.ptr[i] = self.EMPTY
		for i in range(self.N):
			r1 = s1 = self.order[i]
			self.ptr[s1] = -1
			for j in range(4):
				s2 = self.nn[s1][j]
				if self.ptr[s2] != self.EMPTY:
					r2 = self.findroot(s2)
					if r2 != r1:
						if self.ptr[r1] > self.ptr[r2]:
							self.ptr[r2] += self.ptr[r1]
							self.ptr[r1] = r2
							r1 = r2
						else:
							self.ptr[r1] += self.ptr[r2]
							self.ptr[r2] = r1
						if -self.ptr[r1] > big:
							big = -self.ptr[r1]
			if i > 0:
				self.Big[i] = float(big)/float(i)

p = Percolation_NZ()
p.boundaries()
p.permutation()
p.percolate()

array = []
for x in range(p.L):
	temp = []
	for y in range(1,p.L+1):
		temp.append(y+p.L*x)
	array.append(temp)

X = []
Y = []
for order in p.order:
	for x in range(p.L):
		for y in range(p.L):
			if array[x][y] == order:
				X.append(x)
				Y.append(y)

plt.plot(X,Y,'.')
plt.show()