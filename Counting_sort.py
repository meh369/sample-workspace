import time
class CountingSort:
    '''Make a count sort algo using input array and variable derived from it
        Takes input: An array of elements
                     Maximum elements in array
                     Length of Array
    '''
    def __init__(self):
        self.arr = [int(x) for x in input('Enter Comma sep vals: ').split(',')]
        self.max_n = max(self.arr)
        self.len_n = len(self.arr)

    def do_csort(self):

        '''Initiate an empty list with max number + 1 elements
         and then Populate the list with counts at index values
        '''
        count_list = [0]*(self.max_n + 1)
        for i in range(0, self.len_n):
            count_list[self.arr[i]] += 1

        for i in range(1, self.max_n+1):
            count_list[i] = count_list[i] + count_list[i-1]
        
        rearr = [0] * self.len_n
        for i in range(self.len_n-1, -1, -1):
            count_list[self.arr[i]] = count_list[self.arr[i]] - 1
            rearr[count_list[self.arr[i]]] = (self.arr[i]) 
        
        print(f'Sorting {self.arr}...please wait')
        time.sleep(1)
        return  f'finished sorting showing results {rearr}' 

    def __str__(self):
        return 'Counting sort algo'

if __name__=="__main__":
    t = time.time()
    trial = CountingSort()
    print(trial.do_csort())
    p = time.time()-t
    print(f'{trial.__str__()} ran in {p} second(s)')

