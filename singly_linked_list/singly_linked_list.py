
def this_list_is(list):
    return list[0] == None and list[1] == None


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

    def add_to_tail(self, value):
        empty = [self.tail, self.head]

        
        node = Node(value)
        if this_list_is(empty):
            self.head = node
            self.tail = node
        else:
            self.tail.set_next(node)
            self.tail = node
    
    def remove_tail(self):
        empty = [self.tail, self.head]


        if this_list_is(empty):
            return None

        elif self.tail == self.head:
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
        empty = [self.tail, self.head]


        if this_list_is(empty):
            return None
        elif self.tail == self.head:
            val = self.head.get_value()
            self.head = self.head.get_next()
            return val
        else:
            val = self.head.get_value()
            self.head = self.head.get_next()
            return val

    def contains(self, number):
        current = self.head
        print(f'{current}\n')
        while current.value != number:
            if current == None:
                return False
            else:
                current = current.get_next()

        return True

