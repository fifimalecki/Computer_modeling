import random as rnd

N = 100
Nw = 100000

a = 20

x1 = a/2
x2 = -a/2
y1 = a/2
y2 = -a/2

x1C,x2C,y1C,y2C = 0,0,0,0

def wedrowniczek(length):
	global x1,x2,y1,y2,x1C,x2C,y1C,y2C
	x0, y0 = 0,0
	x,y = x0,y0
	walkx,walky = [x],[y]
	while True:
		rand = rnd.randint(1,4)
		if rand == 1:
			x += 1
		elif rand == 2:
			y += 1
		elif rand == 3:
			x += -1
		elif rand == 4: 
			y += -1
		walkx.append(x)
		walky.append(y)
		if x == x1:
			x1C += 1
			return [walkx,walky]
		elif x == x2:
			x2C += 1
			return [walkx,walky]
		elif y == y1:
			y1C += 1
			return [walkx,walky]
		elif y == y2:
			y2C += 1
			return [walkx,walky]
	return [walkx,walky]

for i in range(Nw):
	wedrowniczek(N)

print("x=\t"+str(x1)+"\t:\t"+str(x1C))
print("x=\t"+str(x2)+"\t:\t"+str(x2C))
print("y=\t"+str(y1)+"\t:\t"+str(y1C))
print("y=\t"+str(y2)+"\t:\t"+str(y2C))