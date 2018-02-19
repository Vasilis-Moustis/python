import time
import datetime
now=datetime.datetime.now()


print "current date is:"
print str(now)

d = now.day
m = now.month+1
s = 0            #to sinolo twn idiwn imerwn pou exoun idia imerominia
y = 0 
D = datetime.datetime.today().weekday()
Today = datetime.datetime.today().weekday()
search = datetime.datetime(2018+y, m, now.day).weekday()

print "Current day is: %d" % now.day
print "Current month is: %d" %now.month


for y in range (10):
	if y!=0:
		m=1
	while m<=12:
		if D == datetime.datetime(2018+y, m, now.day).weekday():
			s = s + 1
			m = m + 1
		else:
			m = m + 1
			
			
print "\nto sinolo twn idiwn imerwn pou exoun idia imerominia ta epomena 10 xronia einai:",s







