#Imports
import sys
sys.path.append('binary_search_tree')
sys.path.append('queue/queue.py')
sys.path.append('stack/stack.py')
from bsthelpers import *
from queue import Queue
from stack import Stack

# class Queue:
#         def __init__(self, storage=[]):
#             self.size = 0
#             self.storage = storage
        
#         def __len__(self):
#             return self.size

#         def enqueue(self, value):
#             self.size += 1
#             self.storage.append(value)

#         def dequeue(self):
#             if self.size == 0:
#                 return None
#             else:
#                 self.size -= 1
#                 return self.storage.pop(0)

def park(parent, value, direction):
    node = BSTNode(value)
    # print(parent.value)
    if direction == 'right':
        parent.right = node
    elif direction == 'left':
        parent.left = node
    return node
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    # Insert the given value into the tree
    # def park(self, value):

    def insert(self, value):
        # print(park(self, value, 'left'))
        # park(self, value, 'left')
            # park(value)
        if node_goes_left(self, value):
            if node_can_park_here(self, 'left'):
                park(self, value, 'left')
            else:
                self.left.insert(value)
        elif node_goes_right(self, value):
            if node_can_park_here(self, 'right'):
                park(self, value, 'right')
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target, searching=True):
        if self.value == target and searching:
            return True
        elif searching:
            return pass_it_to_next_node(self, target)
        else:
            raise Exception
        

    # Return the maximum value found in the tree
    def get_max(self):
        max = self.value
        if self.right != None:
            return self.right.get_max()
        
        return max


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left == None:
            print(self.value)
        elif self.right == None:
            print(self.value)
        else:
            self.left.in_order_print()
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        q = Queue()
        q.enqueue(self)
        while len(q) > 0:
            current = q.dequeue()
            #check children
            if current.left != None:
                q.enqueue(current.left)
            if current.right != None:
                q.enqueue(current.right)

            print(current.value)
        


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


# This code is necessary for testing the `print` methods

bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()  
