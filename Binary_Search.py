
class BinarySearch:
    ''' initiate array, lower, upper and position x'''
    
    def __init__(self, arr, tail, head, x):
        self.arr = arr
        self.lower = tail
        self.upper = head
        self.x = x

    def __str__(self):
        return 'Binary Search'
    
    def test(self):
        
        ''' Algo to search the element using list indexing'''
        # sanity check while loop      
        while self.lower <= self.upper:
            #extracting middle element
            mid = (self.lower + (self.upper - 1)) / 2; 
            
            # check for x present at mid
            if self.arr[int(mid)] == self.x:
                return int(mid) 
            # if x is greater, ignore left half
            elif self.arr[int(mid)] < self.x:
                self.lower = int(mid) + 1 # lower is initialised to the rightmost element from the mid 

            elif x < self.arr[int(mid)]:
                self.lower = int(mid) - 1 
        return -1 
        
if __name__ == "__main__":
    import time 
    '''Intialize'''
    x = time.time()
    print("Enter the array with comma separated values which will be searched: ")
    arr = [int(x) for x in input().split(',')]
    x = eval(input("Enter element you want to search in given array..: "))
    
    # Class call 

    result = BinarySearch(arr, 0, len(arr)-1, x)
    t = time.time()
    if result.test() !=-1:
        print(f"Element is present at index {result.test()}")
    else: 
        print("Element not in array")
    p = time.time()-t
    print(f'{result.__str__()} ran in {p}')
