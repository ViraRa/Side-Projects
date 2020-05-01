import sys

class bin_search:

    def __init__(self, arr, key):

        if(not isinstance(arr, list)):
            print("Please specify input as list")
            sys.exit()

        print(self.binary_search(arr, 0, len(arr)-1, key))

        
    def binary_search(self, arr, low, high, key):

        if(low == high): # only has one element in arr
            print("here")
            if(arr[high] == key):
                return high
            else:
                return 0
        else:
            mid = (low + high)//2 # integer division
            if(arr[mid] == key):
                return mid
            if(key > arr[mid]):
                return(self.binary_search(arr, mid+1, high, key))
            else:
                return(self.binary_search(arr, low, mid-1, key))

        
# Here is an example of how to run the program.
# Input a list and a key you want to find
obj = bin_search([1, 2, 3, 4, 5], 1)
