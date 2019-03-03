#!/usr/bin/

################################################
# Dictionary manipultion in Python             #
# Simple Code for understanding purpose only   #
# A dictionary is {key,value}          	       # 
################################################

################################################
# Function to print friend list                #
# Iterates through passed dictionary using key #
################################################
def show_friends(friends):
	'''Function to print hello [friend] '''
	for friendkey in friends:
		print "Hello ", friends[friendkey]
	return
	
		 


#################################################
# main function that defines the dictionary     #
# makes a function call to show friend list     #
#################################################
def my_main():
	'''Entrant function, defining friend list '''
	myfriends_dictionary = {1:"John", 2:"Sam", 3:"Maria"}
	show_friends(myfriends_dictionary)	
	return
	
	

####################################################
# Point of start of execution start,calling main() #
####################################################
my_main()
	




