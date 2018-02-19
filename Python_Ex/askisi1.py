import random



i = 1


players = [[0 for k in range(6)] for l in range(100)]


for x in range (100):
	for u in range (5):
		players[x][u] = random.randint(1,80)

def clean(p):
	for i in range(100):
		p[i][5]=0

def defineS(p):
	x = 0
	for i in range(100):
		if p[i][5]==5:
			x = 1
	return x

S=0
sum=0
print "calculating..."
while i<=1000 :
	i=i+1
	a = []
	a = list(range(1,80))
	random.shuffle(a)
	clean(players)
	S = 0
	while (S==0):
		sum=sum+1
		y = a.pop()
		for k in range(100):
			for l in range(5):
				if players[k][l] == y:
					players[k][5] += 1			
		S = defineS(players)

		

sum = sum/1000
print "o mesos oros kirixis bingo einai ",sum," rolls"

	
	
	
	
	
	
	
	
	
	
	
