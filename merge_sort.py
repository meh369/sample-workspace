
class MergeSort:
    
    def __init__(self):

        self.l = []
        self.n = int(input("enter a number of elements in list: "))
        
    def feedback_call(self):
        '''For loop asking user for input element separately'''

        for i in range(self.n):
            temp = int(input('Enter Element' + str(i + 1) + ': '))
            self.l += [temp]
        

    def feedback_sort(self, a):
        # mid-point (length-1)/2 
        mid = int((len(self.l) - 1)/ 2)
        # check if length is greater than (mid + 2), index starts with value zero 
        if len(self.l) > mid + 2:
            # partition into two parts (a, b)
            a = self.feedback_sort(self.l[0:mid])
            b = self.feedback_sort(self.l[mid:len(self.l)])
        # else check if its only 2 element list
        elif len(self.l) == 2:
            a = [self.l[0]]
            b = [self.l[1]]
        else:
            return self.l
        print(a)
        print(b)         

        # merge in a new list
        c = 0
        v = 0 
        new = []
        # index conditions 
        while (c != len(a) or v != len(b)):
            if c < len(a) and v < len(b):
                if a[c] < b[v]:
                    new.append(a[c])
                    c += 1
                else:
                    new.append(b[v])
                    v += 1

            elif c == len(a) and v != len(b):
                new.append(b[v])
                v += 1

            elif v == len(b) and c != len(a):
                new.append(a[c])
                c += 1

            else: 
                break

        return new 

if __name__ == "__main__":
    merge_sort = MergeSort()
    merge_sort.feedback_call()
    print(merge_sort.feedback_sort([]))