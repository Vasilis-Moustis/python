import time
import datetime
import calendar
now=datetime.datetime.now()


print "current date is:"
print str(now)

d = now.day
m = now.month+1
s = 0            #to sinolo twn idiwn imerwn pou exoun idia imerominia
y = 0 
D = calendar.weekday(2018, m, d)

print "Current day is: %d" % now.day
print "Current month is: %d" %now.month

for y in range (10):
	if y!=0:
		m=1
	while m<=12:
		if D == calendar.weekday(2018+y, m, now.day):
			s = s + 1
			m = m + 1
		else:
			m = m + 1
			
			
print "\nto sinolo twn idiwn imerwn pou exoun idia imerominia einai: "
print s
