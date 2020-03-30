
class PascalTriangle:

    def __init__(self):
        self.num = int(input("Enter a number to enumerate Pascal's list: "))
        self.list_1 = []

    def populate_list(self):
        self.list_1.append(1)
        i = 1
        
        while (i <= self.num):
            k = 1
            l = []
            l.append(1)
            
            while(k < i):
                l.append(self.list_1[i - 1][k] + self.list_1[i - 1][k - 1])
                k = k + 1
            
            l.append(1)
            self.list_1.append(l)
            i = i + 1
        
        return self.list_1   

    def binomial_coeff(self):
        j = int(input("Enter an index number to extract element from the Pasal's list: "))
        pascal_tri = self.populate_list()
        # print(pascal_tri[self.num])
        return (pascal_tri[self.num][j - 1])

    def __str__(self):
        
        return f'number selected is {self.num} and pascal triangle is \n {self.populate_list()}'

if __name__ == "__main__":
    a = PascalTriangle()
    print(a)
    # print(a.populate_list())
    print(a.binomial_coeff())
    