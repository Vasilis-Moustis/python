import random
import sqlite3
import string



table = [[0 for k in range(100)] for l in range(100)]

mystring = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

for i in range(100):
	for j in range (100):
		table[i][j] = random.choice(mystring)

print "reading dictionary.txt"		

f = open('dictionary.txt', 'r')

print "dictionary read"

dictionary = [line[0:-1] for line in f]
found = [0 for line in f]


def foundyou(t,d,i,j,k):
	S = 0
	H = 1 #orizontia
	V = 1 #katheta
	D = 1 #diagwnia
	I = 0
	f = i
	g = j
	while I<=len(d[k]) and (i+len(d[k])-I)<=99:
		if d[k][I-1]!=t[i][j]:
			H = 0
		I = I + 1
		i = i + 1
	I=0
	i = f
	j = g
	while I<=len(d[k]) and (j+len(d[k])-I)<=99:
		if d[k][I-1]!=t[i][j]:
			V = 0
		I = I + 1
		j = j + 1
	I = 0
	i = f
	j = g
	while I<=len(d[k]) and (i+len(d[k])-I)<=99 and (j+len(d[k])-I)<=99:
		if d[k][I-1]!=t[i][j]:
			H = 0
		I = I + 1
		i = i+1
		j = j + 1
	if H==1 or V==1 or D==1:
		print dictionary[k]
	return S

z = 0
x = 0
w = 0

print "arxi anazitisis lexewn>>>>"

for z in range(100):
	for x in range (100):
		for w in range (len(dictionary)):
			if dictionary[w][1]==table[z][x]:
				foundyou(table,dictionary,z,x,w)

print ">>>>telos anazitisis lexewn"


