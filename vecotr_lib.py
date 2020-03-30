import math
import random

class Vector: 
    
    def __init__(self, components):
        self.component = components

    def set(self,  new_components):
        if len(self.components)> 0:
            self._components = new_components 
        else: 
            raise Exception("Please give any vector")

    def __str__(self):
        return f"{self._components}"
    
    def component(self, i):
        
        if i < len(self._components) and i >= 0:
            return self._components[i]
        else: 
            raise Exception("Index out of range!")
        
    def size(self):
        return len(self._components)

    def euclidean_norm(self):
        """Square root of sum of squares of unit vecto"""
        elen = []
        for i in self._components:
            elen += i ** 2 
        return math.sqrt(elen)

    def __add__(self, *args):
        size =  self.size()
        add =  []
        if size == args.size():
            for i in range(size):
                add.append(self._components[i] + args[i])
        else: 
            raise Exception("Must have same size")

        return Vector(add)
    
if __name__ == "__main":
    a = Vector([3,2,1])
    a.set(4)
    print(a._components())
    print(a)