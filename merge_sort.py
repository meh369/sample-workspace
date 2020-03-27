class MergeSort:
    def __init__(self):
        self.l = []
        self.n = int(input("enter a number of elements in list: "))
        

    def call(self):
        for i in range(self.n):
            temp = int(input('Enter Element' + str(i + 1) + ': '))
            self.l += [temp]
    
    def sort(self, L=None):
        mid = int((len(self.l) - 1)/ 2)

        if len(self.l) > mid + 2:
            a = self.sort(self.l[0:mid])
            b = self.sort(self.l[mid:len(self.l)])

        elif len(self.l) == 2:
            a = [self.l[0]]
            b = [self.l[1]]

        else:
            return self.l

        c = 0
        v = 0 
        new = []
        while (c != len(a) or v != len(b)):
            if c < len(a) and v < len(b):
                if a[c] < b[v]:
                    new += [a[c]]
                    c += 1

                else:
                    new += [b[v]]
                    v += 1

            elif c == len(a) and v != len(b):
                new += [b[v]]
                v += 1

            elif v == len(b) and c != len(a):
                new += [a[c]]
                c += 1

            else: 
                break

        return new 


if __name__ == "__main__":
    merge_sort = MergeSort()
    merge_sort.call()
    print(merge_sort.sort(MergeSort))