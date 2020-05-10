class DP_FIB_Memo:

    memo = [1, 1] # for index zero and one

    def __init__(self):
        
        # intentionally blank
        pass 

    def fib_num(self, n):

        if(n < 0):
            raise ValueError("Number should be positive or 0")
    
        if(isinstance(n, int)):

            if(n == 0):
                return 0
            else:
                for x in range(2, n):

                    self.memo.append(self.memo[x - 1] + self.memo[x - 2])
        else:
            raise ValueError("Input value should be integers")

        return self.memo[-1]


obj = DP_FIB_Memo()

############################################ Unit Test #####################################################
import unittest
from Fib_DB import DP_FIB_Memo
# the source file is called Fib_DB and its class is DP_FIB_Memo

class TestFib(unittest.TestCase):

    # Simple unit test for fibonacci sequence using unittest library 
    
    def test_fib_num(self): # testing the fib_num  method

        obj = DP_FIB_Memo()

        self.assertEqual(obj.fib_num(0), 0) # checking if fib(0) = 0

        with self.assertRaises(ValueError): # checking if fib(- num) raises an error
            obj.fib_num(-1)

        with self.assertRaises(ValueError): # checking if it raises error when n is not an integer
            obj.fib_num(2.0)
        
if __name__ == "__main__":
    unittest.main()
