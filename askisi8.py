import random
a = []
for i in range (30):
	x = random.randint(-30,30)
	a.append(x)

print a
print "oi triades me athroisma miden einai: "

S = 0
for j in range (30):
	for k in range (30):
		for g in range (30):
			if (a[j]+a[k]+a[g]==0):
				S=1
				print a[j]," ",a[k]," ",a[g]

if (S==0):
	print " dn vrethikan tetoioi sindiasmoi"

	
