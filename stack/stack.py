"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?

   Performance in the linked list is better when 
"""


I_want_to_test = 'LinkedList Implementation'


#Which one are you testing? : 'List Implementation' 'LinkedList Implementation'

if I_want_to_test == 'List Implementation':









    #List
    class Stack:
        def __init__(self, storage=[]):
            self.size = 0
            self.storage = storage

        def __len__(self):
            return self.size

        def push(self, value):
            self.size += 1
            self.storage.append(value)

        def pop(self):
            if self.size == 0:
                return None
            else:
                self.size -= 1
                return self.storage.pop()









elif I_want_to_test == 'LinkedList Implementation':

    #Imports
    import sys
    sys.path.append('/home/ferror18/Documents/Lambda/Data-Structures')
    from singly_linked_list.singly_linked_list import LinkedList












    #Linked List
    class Stack:
        def __init__(self, storage=LinkedList()):
            self.size = 0
            self.storage = storage

        def __len__(self):
            return self.size

        def push(self, value):
            self.size += 1
            self.storage.add_to_tail(value)

        def pop(self):
            if self.size == 0:
                return None
            else:
                self.size -= 1
                return self.storage.remove_tail()










#Umbrella
else:
    print('Please provide a valid imp to test')