class Node:
    def __str__(self):
        return f'''Value: {self.value} | Next: {self.next_node}'''
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value
        
    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __str__(self):
        return f'''
        Head: {self.head } \n
        Tail: {self.tail} '''

    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        return self.head == None and self.head == None

    def has_only_one_node(self):
        return self.head == self.tail

    def add_to_tail(self, value):
        node = Node(value)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.set_next(node)
            self.tail = node
    
    def remove_tail(self):
        if self.is_empty():
            return None

        elif self.has_only_one_node():
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val
        else:
            val = self.tail.get_value()
            current = self.head
            while current.get_next() != self.tail:
                current = current.get_next()
            
            self.tail = current
            self.tail.set_next(None)
            return val
    
    def remove_head(self):
        if self.is_empty():
            return None
        elif self.has_only_one_node():
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val
        else:
            val = self.head.get_value()
            self.head = self.head.get_next()
            return val

    def contains(self, number):
        current = self.head
        if self.is_empty():
            return False
        
        while current != None:
            if current.get_value() == number:
                return True
            else:
                current = current.get_next()
        return False
