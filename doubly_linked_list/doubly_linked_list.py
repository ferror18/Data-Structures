"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __str__(self):
        return f'Value:{self.value}\tPrev:{self.prev}\tNext:{self.next}\n'
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __str__(self):
        current = self.head
        values = []
        while current != None:
            values.append(current.value)
            current = current.next
        return str(values)

    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    

    def is_empty(self):
        return self.head == None and self.head == None


    def has_only_one_node(self):
        return self.head == self.tail

    def add_first_node(self, value):
            node = ListNode(value)
            self.head = node
            self.tail = node
            self.length += 1
    def delete_last_node(self):
            #Grab value
            deleted_node = self.head.value
            #List poniters
            self.head = None
            self.tail = None
            self.length -= 1
            return deleted_node
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        
        if self.is_empty():
            self.add_first_node(value)
        else:
            node = ListNode(value, None, self.head)
            self.length += 1
            self.head = node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.is_empty():
            return None
        elif self.has_only_one_node():
            return self.delete_last_node()
        else:
            #Grab value
            deleted_node = self.head.value
            #List poniters
            self.head = self.head.next
            # Node changes
            self.head.prev = None
            self.length -= 1
            return deleted_node
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if self.is_empty():
            self.add_first_node(value)
        else:
            #Create Node
            node = ListNode(value, self.tail)
            #changes to list
            self.tail.next = node
            self.length += 1
            #Changes to nodes
            self.tail = node
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.is_empty():
            return None
        elif self.has_only_one_node():
            return self.delete_last_node()
        else:
            #Grab value
            deleted_node = self.tail.value
            #List poniters
            self.tail = self.tail.prev
            # Node changes
            self.tail.next = None
            self.length -= 1
            return deleted_node
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node == self.head:
            return None
        else:
            #Node neigbors
            if self.tail == node:
                self.tail = node.prev
            if node.prev is not None:
                node.prev.next = node.next
            if node.next is not None:
                node.next.prev = node.prev
            #node
            node.prev = None
            node.next = self.head
            self.head.prev = node
            #list changes
            self.head = node

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node == self.tail:
            return None
        else:
            #Node neigbors
            if self.head == node:
                self.head = node.next
            if node.prev != None:
                node.prev.next = node.next
            if node.next != None:
                node.next.prev = node.prev
            #node
            node.next = None
            node.prev = self.tail
            self.tail.next = node
            #list changes
            self.tail = node
            
    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.is_empty():
            return None
        elif self.has_only_one_node():
            return self.delete_last_node()
        else:
                #Node neigbors
            if node.prev != None:
                node.prev.next = node.next
            if node.next != None:
                node.next.prev = node.prev
            #List
            if self.head == node:
                self.head = node.next
            if self.tail == node:
                self.tail = node.prev
            self.length -= 1
            # node
            node.next = None
            node.prev = None
        return node

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.is_empty():
            return
        else:
            max = self.head.value
            current = self.head.next
            while current:
                if current.value > max:
                    max = current.value
                current = current.next
            return max

# Hi guys, i think one of the test might be testing the incorrect thing 
# pls let me know if im wrong. It is line 80 for DoubleLinked list:
# 79# self.dll.move_to_end(self.dll.head.next)
# 80# self.assertEqual(self.dll.tail.value, 40)
# at this point in the the test there is only 2 nodes on the list
# head has value 40 and tail has value 4
# line 79 by calling move_to_end on head.next it moves the tail back into tail
# the tail value remains 4 and so the assertion fails on line 80
# I believe correct test would be 79# self.dll.move_to_end(self.dll.head)
# removing the .next
