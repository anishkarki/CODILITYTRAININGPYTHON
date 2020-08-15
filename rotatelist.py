import unittest
import random
array_range= (-1000,1000)
INT_range=(0,100)


def solution(A,K):
    if not len(A):
        return A
    cutouts = (len(A)+K)%len(A)
    if cutouts>0:
        head = A[len(A)-cutouts:]
        tail = A[:-cutouts]
        return head+tail
    else:
        return A


class TestCyclicRotation(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(solution([6,3,8,9,7],0),[6,3,8,9,7])
    
    def test_example1(self):
        self.assertEqual(solution([3, 8, 9, 7, 6], 3), [9, 7, 6, 3, 8])

    
    def test_random(self):
        N = random.randint(*INT_range)
        K = random.randint(*INT_range)
        A = [random.randint(*array_range) for i in range(0,N)]
        print(N,K,A)
        print(solution(A,K))

if __name__=='__main__':
    unittest.main()