#!/usr/bin/

####################################
# Playing with Classes in Python   #
# A dummy Class for practice       #
####################################


####################################
# defining class for makeup        #
####################################
class makeup:
	itemtype = "eyemakeup"
	eyelinercolour = "black"
	
	def __init__(self,userselecteditemtype):
		self.itemtype = userselecteditemtype

	def geteyelinercolour(self,colour):
		self.eyelinercolour = colour

	def showitemtype(self):
		print "Item selected is ", self.itemtype


	
	
			
	
#######################################
# defining the main entrant function  #	 
#######################################
def my_main():
	makeupinstance = makeup("blushon")
	makeupinstance.showitemtype()
	
	

########################################
# calling main() to begin the execution#
########################################  
my_main()
	
