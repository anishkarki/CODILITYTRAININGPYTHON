#Binary Gap
import unittest
#from stackclass import StackDeclare
from collections import deque

MAXINT = 2147483647

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


def solution(N):
    count=0
    lastcount=0
    countstack = StackDeclare()
    while (N>0):
        val = N//2
        num = N%2
        N = val
        if num == 1:        
            if countstack.peek() != 1:
                countstack.push(num)
            else:
                countstack.pop()
                if lastcount <= count:
                    lastcount=count
                count = 0
                countstack.push(num)
        elif num == 0:
            if countstack.peek() == 1:
                count += 1
            else:
                pass
    return lastcount

print (solution(74901729))

class TestGap(unittest.TestCase):
    def test_example(self):
        self.assertEqual(5, solution(1041)) 

    def test_example2(self):
        self.assertEqual(0,solution(32))

    def test_extremes(self):
        self.assertEqual(0,solution(1))
        self.assertEqual(1,solution(5))
        self.assertEqual(0,solution(MAXINT))    


if __name__ == '__main__':
    unittest.main()
    solution(1)
        

