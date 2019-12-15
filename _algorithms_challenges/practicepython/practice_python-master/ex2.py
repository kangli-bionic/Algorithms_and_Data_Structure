#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3

'''
Ex 2:

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

(1) If the number is a multiple of 4, print out a different message.
(2) Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''

def main():
	import sys
	
	# Get user input
	str = input("Please enter an integer: ")
	num = int(float(str))  # force the input to an int

	# Part the first
	if num % 2 == 0:
		print ('Your number is even.')
	else:
		print ('Your number is odd.')

	# Part the second
	if num % 4 == 0:
		print ('Your number is a multiple of 4.')

	# Part the third
	str1 = input("\nPlease enter an integer numerator: ")
	str2 = input("Please enter an integer denominator: ")
	# force both inputs to integers
	numerator = int(float(str1))
	denominator = int(float(str2))
	if denominator == 0:
		print ('Cannot accept zero divisor. Exiting.')
		sys.exit()
	else:
		if numerator % denominator == 0:
			print ("{} divides evenly into {}".format(denominator, numerator))
		else:
			print ("{} does not divide evenly into {}".format(denominator, numerator))

	

if __name__ == "__main__":
	main()