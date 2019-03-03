#!/usr/bin

'''
This is a simple python program depicting the process
of bubble sort.This is for learning purpose only.

bubble Sort is a sorting algorithm, to arrange items
in a order.
Why sort? If items are arranged in a sorted manner, 
search operations are more efficient.
Logic: It works by repeatedly swapping the adjacent 
elements if they are in the wrong order.

'''


'''
This function compares the adjacent numbers, and swaps
them if they are in the wrong order
'''
def bubSort(data):
	numberItems = len(data)
	for outerIter in range(numberItems):
		for innerIter in range(0, numberItems-outerIter-1):
			if data[innerIter] > data[innerIter+1]:
				data[innerIter], data[innerIter+1]=data[innerIter+1], data[innerIter]




'''
This function takes input from user, 8 numbers to be sorted
'''
def my_main():
	inputList=[]
	for i in range(1,8):
		userData = raw_input("Please enter the array to be sorted: ")
		inputList.append(userData)
	
	print "You entered: ", inputList
	bubSort(inputList)
	print "Sorted List: ", inputList


#Start of execution
my_main()

	
	
