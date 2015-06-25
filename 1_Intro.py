"""Create a program (a .py file) which repeatedly asks the user for a word. The program should append all the words together. When the user types a "!", "?", or a ".", the program should print the resulting sentence and exit.
For example, a session might look like this:
[~]$ python breakout01.py
Enter a word (. ! or ? to end): My
Enter a word (. ! or ? to end): name
Enter a word (. ! or ? to end): is
Enter a word (. ! or ? to end): Walter
Enter a word (. ! or ? to end): White
Enter a word (. ! or ? to end): !

My name is Walter White!"""


def stringCat(fin,s = list(),w = ""):
	while w not in fin:
		w = raw_input("Enter a word (. ! or ? to end):")
		if w in fin: s.append("\b"+w)
		else: s.append(w)
    	#s.append(w)
	return " ".join(s)

fin = [".", "?", "!"]
print stringCat(fin)


"""Write a program that prints the numbers from 1 to 100. 
But for multiples of three print "Fizz" instead of the number and for the 
multiples of five print "Buzz". 
For numbers which are multiples of both three and five print "FizzBuzz".
If you finish quickly... see how few characters you can write this program in (this is known as "code golf": going for the fewest key strokes)."""

def fizzbuzz(end):
	for x in xrange(1,end):
		mult3 = x % 3 == 0
		mult5 = x % 5 == 0
		if mult3 and mult5:
			print "FizzBuzz"
		elif mult3:
			print "Fizz"
		elif mult5:
			print "Buzz"
		else:
			print x
	
print fizzbuzz(100)
