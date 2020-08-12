"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


I_want_to_test = 'LinkedList Implementation'


#Which one are you testing? : 'List Implementation' 'LinkedList Implementation'

if I_want_to_test == 'List Implementation':



    #List
    class Queue:
        def __init__(self, storage=[]):
            self.size = 0
            self.storage = storage
        
        def __len__(self):
            return self.size

        def enqueue(self, value):
            self.size += 1
            self.storage.append(value)

        def dequeue(self):
            if self.size == 0:
                return None
            else:
                self.size -= 1
                return self.storage.pop(0)






elif I_want_to_test == 'LinkedList Implementation':

    #Imports
    import sys
    sys.path.append('/home/ferror18/Documents/Lambda/Data-Structures')
    from singly_linked_list.singly_linked_list import LinkedList









    #Linked List
    class Queue:
        def __init__(self, storage=LinkedList()):
            self.size = 0
            self.storage = storage
        
        def __len__(self):
            return self.size

        def enqueue(self, value):
            self.size += 1
            self.storage.add_to_tail(value)

        def dequeue(self):
            if self.size == 0:
                return None
            else:
                self.size -= 1
                return self.storage.remove_head()











#Umbrella
else:
    print('Please provide a valid imp to test')