 #!/usr/bin/

'''
Simple program to show recursion in python. It is 
only for practice.
'''

'''
function that calculates factorial of a number.
factorial N = N*N-1*N-2*...*1
'''
def fact(number):
	if number == 1:#last iteration
		return 1
	else:#for all numbers greater than 1
		print "Number is: ", number
		return number * fact(number-1)
		
	
'''
My custom main function, which is called to start
execution.
'''
def my_main():
	user_input=raw_input("Please enter the number for factorial calculation: ")
	value = fact(int(user_input))
	print "value of factorial is:", value

	
#start execution
my_main()

	
