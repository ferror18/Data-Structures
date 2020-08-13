
def node_can_park_here(parent, direction):
    if direction == 'left':
        if parent.left == None:
            return True
        else:
            return False
    elif parent.right == None:
        if parent.right == None:
            return True
        else:
            return False

def node_goes_left(self, value):
    if self.value > value:
        return True
    else:
        return None

def node_goes_right(self, value):
    if self.value <= value:
        return True
    else:
        return None


def pass_it_to_next_node(parent, value):
    if parent.value > value:
        if parent.left == None:
            return False
        else:
            return parent.left.contains(value)
    if parent.value <= value:
        if parent.right == None:
            return False
        else:
            return parent.right.contains(value)