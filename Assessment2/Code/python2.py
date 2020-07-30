	# INSTRUCTIONS

	# In case it is not clear, the Question appears first, then examples, then any hints and finally the function that you need to complete appears underneath:

	# <QUESTION>

	# <EXAMPLES>

	# <HINT>

	# You are allowed access to the internet for this assessment, you can also use the DOCUMENTATION that comes bundled with your Python installation.  You should already be comfortable accessing this documentation, but to summarise:

	# Access Python from you CLI by typing python or python3

	# Type help() or for example help(str) on your Python terminal

	# To leave a Python terminal type exit()



	# <QUESTION 1>    
	
	# Given a string, return a string where for every char in the original string, there are three chars.
	
	# <EXAMPLES>

	# one("The") → "TTThhheee"
	# one("AAbb") → "AAAAAAbbbbbb"
	# one("Hi-There") → "HHHiii---TTThhheeerrreee"

	# <HINT>
	# How does a for loop iterate through a string?

def one(input):
	n = ""
	for i in input:
		n = n + (i*3)
	return n

	# <QUESTION 2>

	#  Write a function which returns the boolean True if the input is only divisible by one and itself.
	
	# The function should return the boolean False if not.

	# <EXAMPLES>

	# two(3) → True
	# two(8) → False

	# <HINT>
	# What operator will give you the remainder?
	# Use your CLI to access the Python documentation and get help manipulating strings - help(range).

def two(input):

# prime number is always greater than 1
	if input > 1:
		for i in range(2, input):
			if (input % i) == 0:
				l = False
				break
		else:
			l = True

		return l
	else:
		return False

# if the entered number is less than or equal to 1
# then it is not prime number

	# <QUESTION 3>

	# Write a function which takes an integer input, a, and returns the sum a+aa+aaa+aaaa.

	# So if 2 was the input, the function should return 2+22+222+2222 which is 2468.

	# <EXAMPLES>

	# three(9) → 11106
	# three(5) → 6170

	# <HINT>
	# What happens if you multiply a string by a number?

def three(a):
	x = str(a)
	final = int(x) + int(x*2) + int(x*3) + int(x*4)

	return final
	

	# <QUESTION 4>

	# Given two Strings of equal length, 'merge' them into one String.

	# Do this by 'zipping' the Strings together.

	# Start with the first char of the first String.
	# Then add the first char from the second String.
	# Then add the second char from the first String.
	# And so on.

	# Maintain case.

	# You will not encounter whitespace.
	
	# <EXAMPLES>

	# four("String","Fridge") → "SFtrriidngge"
	# four("Dog","Cat") → "DCoagt"
	# four("True","Tree") → "TTrrueee" 
	# four("return","letter") → "rleettutrenr"

	# <HINT>
	# Use your CLI to access the Python documentation and get help manipulating strings - help(list.insert).
	# How would you seperate a string into characters?

def four(input1, input2):
	x = list(input1)
	y = list(input2)
	z = ''

	for i in range (len(x)):
		z = z + x[i]
		z = z + y[i]

	return z

	# <QUESTION 5>

	# Write a function to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
	
	# <EXAMPLES>
	
	# five() → [100,102,122,198,200]
	# five() → [108,104,106,188,200]
	# five() → [154,102,132,178,164]
	
	# <HINT>
	# There is a module which can be used to generate random numbers, this module is called random.
	# The random module contains a function called randint.
import random
def five():
	l = []
	for x in range(5):
		
		l.append(random.randrange(100, 200, 2))
	return l

	# <QUESTION 6>

	# Given a string, return the boolean True if it ends in "py", and False if not. 
	
	# Ignore Case.

	# For Example:

	# six("ilovepy") → True
	# six("welovepy") → True
	# six("welovepyforreal") → False
	# six("pyiscool") → False

	# <HINT>
	# There are no hints for this question.
	
def six(input):
	input = input.lower()
	if input[-2:] == 'py':
		return True
	else:

		return False

	# <QUESTION 7>

	# Given three ints, a b c, one of them is small, one is medium and one is large. 
	
	# Return the boolean True if the three values are evenly spaced, so the
	# difference between small and medium is the same as the difference between
	# medium and large. 
	
	# Do not assume the ints will come to you in a reasonable order.
	
	# <EXAMPLES>

	# seven(2, 4, 6) → True
	# seven(4, 6, 2) → True
	# seven(4, 6, 3) → False
	# seven(4, 60, 9) → False

	# <HINT>
	# There is a function for lists called sort.
	# Use the cli to access the documentation help(list.sort)

def seven(a, b, c):
	l =[]
	l.append(a)
	l.append(b)
	l.append(c)

	l.sort()
	if l[0] + l[1] == l[2] or l[0] == l[2]:
		return True
	else:
		return False



	# <QUESTION 8>

	# Given a string and an integer, n, return a string that removes n letters from the 'middle' of the string.
	
	# The string length will be at least n, and be odd when the length of the input is odd, so there will always be a 'middle'.

	# <EXAMPLES>

	# eight("Hello", 3) → "Ho"
	# eight("Chocolate", 3) → "Choate"
	# eight("Chocolate", 1) → "Choclate"

	# <HINT>
	# Use the cli to access the documentation help(str.replace)

def eight(input,  a):
	return ""

	# <QUESTION 9>

	# Given two string inputs, if one can be made from the other return the boolean True, if not return the boolean False.

	# <EXAMPLES>

	# nine("god", "dog") → True
	# nine("tree", "tiredest") → True
	# nine("cat", "dog") → False
	# nine("tripping", "gin") → True

	# <HINT> 
	# There are no hints for this question.

def nine(string1, string2):
	
	if list(string1) in list(string2):
		return True
	else:
		return False





	# <QUESTION 10>

	# Write a function which takes 2 integers greater than 0, X,Y as input and generates a 2-dimensional array. 
	
	# The element value in the i-th row and j-th column of the array should be i*j.

	# <EXAMPLES>

	# ten(3,2) → [[0,0,0],[0,1,2]]
	# ten(2,1) → [[0,0]]
	# ten(3,4) → [[0,0,0],[0,1,2],[0,2,4],[0,3,6]]

	# <HINT>
	# Think about nesting for loops.

def ten(X,Y):
	l = []
	for i in range(0, Y):


		l.append([])
		
		for n in range(0, X):
			l[i].append(n * i)
			
	return l