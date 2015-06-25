"""This breakout will give you a chance to explore some of the builtin modules offered by Python. For this session, please use your text editor to create the files. You'll have to
Create and edit a new file called age.py. Though you can do this via the %%file magic used above, here you should use your text editor.
within age.py, import the datetime module
use datetime.datetime() to create a variable representing your birthday
use datetime.datetime.now() to create a variable representing the present date
subtract the two (this forms a datetime.timedelta() object) and print that variable.
Use this object to answer these questions:
How many days have you been alive?
How many hours have you been alive?
What will be the date 1000 days from now?
Create and edit a new file called age1.py. When run from the command-line with one argument, age1.py should print out the date in that many days from now. If run with three arguments, print the time in days since that date.
[~]$ python age1.py 1000
date in 1000 days 2016-06-06 14:46:09.548831

[~]$ python age1.py 1981 6 12
days since then: 11779"""

import datetime
import sys

def bdDiff(year,mon,day):
	bd =  datetime.datetime(year,mon,day)
	now = datetime.datetime.now()
	diff = (now - bd)
	d = diff.days
	return "days since {0}-{1}-{2}: {3}".format(year,mon,day, d)

def futureDate(d):
	now = datetime.datetime.now()
	fut = now + datetime.timedelta(d)
	return "date in {0} days {1}".format(d,fut)


argLen = len(sys.argv)
args = sys.argv

if argLen == 2:
	print futureDate(int(args[1]))
elif argLen == 4:
	print bdDiff(int(args[1]),int(args[2]),int(args[3]))
else:
	print "Fuck Off and do it properly"