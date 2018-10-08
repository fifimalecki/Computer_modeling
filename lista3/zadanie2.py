import matplotlib.pyplot as plt
import random as rnd

N = 1000

def wedrowniczek(length):
	x0, y0 = 0,0
	x,y = x0,y0
	walkx,walky = [x],[y]
	positions = []
	stepsCounter = 0
	for i in range(length):
		positions.append([walkx[-1],walky[-1]])
		s = [
			[walkx[-1]+1,walky[-1]],
			[walkx[-1],walky[-1]+1],
			[walkx[-1]-1,walky[-1]],
			[walkx[-1],walky[-1]-1]
			]
		possibleNodes = []
		for possible in s:
			if possible not in positions:
				possibleNodes.append(possible)
		if len(possibleNodes) > 0:
			rand = rnd.randint(0,len(possibleNodes)-1)
			x = possibleNodes[rand][0]
			y = possibleNodes[rand][1]
			stepsCounter += 1
		else:
			return [walkx,walky],stepsCounter

		walkx.append(x)
		walky.append(y)
	return [walkx,walky], stepsCounter
maxReach = 741
longestSteps = 0
counter = 0
walks = []
while(longestSteps < maxReach):
	walk, stepsCounter = wedrowniczek(N)
	counter += 1
	if stepsCounter > longestSteps:
		longestSteps = stepsCounter
		walks = walk
		print(longestSteps, counter)
plt.plot(walks[0],walks[1])
plt.title(str(longestSteps)+" kroków. "+str(counter)+"-ty wędrowniczek")
plt.grid()
plt.show()
