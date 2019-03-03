#!/usr/bin/

######################################################
# Python Condional statements usage                  #
# This is simple code for practice only              #
# Using 'if/else','for' and 'while' loops            #
######################################################

######################################################
# Imports
######################################################

from datetime import date
######################################################

######################################################
# prints the whole date or month, as per user input  #
# demonstrates use of for loop and if/else statement #
######################################################
def print_date():
	user_input=raw_input("input 1: date, 2: month--")
	#  use of if/elif/else loop
	if user_input == '1':
		print "Today is: ", date.today()
	elif user_input == '2':
		month_dic={1:"Jan",2:"Feb", 3:"March", 4:"April"}
		my_month = date.today().month
		# use of for loop
		for month_iter in month_dic:
			if month_iter == my_month:
				print "This is the month of ", month_dic[month_iter]
				break
	else:
		print "Invalid Input from you "
	return 
	
######################################################
	

######################################################
# custom main function                               #
# Uses while loop for user input                     #
######################################################

def my_main():
	if __name__ == "__main__":
		# use of while loop
		while True:
			proceed = raw_input ("Hello User, Do you want to Proceed y/n: ")
			if proceed == 'n':
				break
			print_date()
	return
	
######################################################

#####################################################
#start of execution
#####################################################
my_main()	
	
# End
	
		
