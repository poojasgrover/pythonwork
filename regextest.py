#!/usr/bin/

#######################################################
#						      #
# Simple code to use regular expressions              #
# for parsing etc. This is for practice only	      #
#						      #
#######################################################

#######################################################
# importing the re module                             #
#######################################################
import re


######################################################
# check if string starts with given word(it)         #
######################################################

txt = "It is all in the game"
x = re.search("^It", txt)

if (x):
  print("Yes. Sring begins with 'it'")
else:
  print("No match")

######################################################
# check if string ends with given word(butter)       #
######################################################

mystr = "Betty bought a bit of butter"
y = re.findall("butter$",mystr)
if (y):
	print("Yes. butter is the last word")
else:
	print("Sorry, the condition is invalid")
print(y)

######################################################
# check if string contains 'in'                      #
######################################################
mystr2 = "in pin safety pin"
z = re.findall("inx*",mystr2)
if (z):
	print("Yes. 'in' is present")
else:
	print("Sorry, the condition is invalid")
print(z)

######################################################
# check if string has words with 'a' and 2 'l'       #
######################################################
mystr3 = "wall is tall in the hall"
a = re.findall("al{2}",mystr3)
if (a):
	print("Yes. words containing 'all' present")
else:
	print("Sorry, the condition is invalid")
print(a)

#end
