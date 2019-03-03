#!/usr/bin

'''

Simple Implementaion of Binary Search Tree in Python.
This is just for learning purpose. 

Binary Tree: It is a tree data structure with a parent
node, that has atmost 2 child nodes.

Binary Searh Tree (BST): This is a binary tree, with the left
child value less than the parent, and right child value
greater than that of the parent.

'''
'''
Requirement:
for insertion
1. create root node. Save this node for lifetime of app.
2. add the next node to left child, if value less 
than root node. if the value is greater than root node,
add to the right node.
3. for the next element, if it is less than the parent and less
than the left child, then
make it a left child, of the current child. If it is less than the parent,
and more than the left child, it will be the right child, of the current
left child.
Similarly, if it is more than parent node, but less than the left child, then
the new element will be added as a left child of the right child. If it is
more than the parent, and more than the current right child, then make it
the right child of the current child.
4. similar steps if the value is more than the root node.
for search:
1. get the number to be searched.
2. compare it with the value at the root node. if found, end the search.
3. if the value is less than the root, search the left branch. If the value
is more than the root value, search the right branch.
4. Compare the node value, with the element to be searched, till a match
is found or the leaf node is reached. 

for deleting:
1. compare the value with thw root node value. If found, delete it.
Else if the value is less than the root node, traverse the left tree.
If found, delete the node, and readjust tne childnodes.

for traversal:
1. traversal can be inorder, preorder or post order.
'''
'''
functions needed:
1. insertBST: This should add a new node into the tree.If it's the first node,
make it root. Then, for the next element check if the value is less or more than
the root. If it is less, then insert as left child, else right.
2. searchBST: This should search, if same as root, return immediately. Else, if
less than left node, search left tree. Otherwise, search right tree.
3. printBST: print all the elements of the tree. 
 
'''
class myBST:
	def __init__(self,instValue):
		self.value = instValue
		print "adding: ",self.value
		self.leftChild = None 
		self.rightChild = None
		return
		
	
	def insertBST(self, value):
		print "value of root: ", self.value
		print"value of child: ", value	
		print"flag test: ",self.value < value
		if self.value > value:
			print "root val in left: ", self.value
			print "child val in left : ", value
			if self.leftChild is None:
				print "inserting left child to root...."
				self.leftchild = myBST(value)
			else:
				print "inserting left child to next.."
				self.leftChild.insertBST(value)
		elif self.value < value:
			print "root val in right: ", self.value
			print "child val in right: ", value
			if self.rightChild is None:
				print "inserting right child to root.."
				self.rightChild=myBST(value)
			else:
				print "inserting right child to next.."
				self.rightChild.insertBST(value)	
		else:
			print " Repeat value"

		return

	def searchBST(self,value):
		print "Hello Search"
		return

		
	def printBST(self):
		if self.leftChild :
			self.leftChild.printBST()
		print "Data is: ",self.value
			
		if self.rightChild:
			self.rightChild.printBST()
		return
				
		
		



def my_main():
	#create root element
	rootNode = myBST('10')
	
	#add elements to the list
	rootNode.insertBST('9')
	rootNode.insertBST('12')
	#rootNode.insertBST('5')

	rootNode.printBST()
	

#calling my_main to start execution
my_main()

