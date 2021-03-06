from collections import deque

class StackDeclare:
    def __init__(self):
        self.items = deque()
    
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if (len(self.items)>0):
            return self.items.pop()
        else:
            return None

    def peek(self):
        if (len(self.items)>0):
            return self.items[len(self.items)-1]
        else:
            return None
    
    def size(self):
        return len(self.items)
