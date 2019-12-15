#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3

'''
List a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line
of Python that takes this list a and makes a new list that has only
the even elements of this list in it. 
'''

def main():
	a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
	
	e = [elem for elem in a if a.index(elem) % 2 == 0]
	
	print ("Even list is: {}".format(e)) 
		
if __name__ == "__main__":
	main()