import ctypes


class DynamicArray:
    
    def __init__(self) -> None:
        self.n = 0; #count of actual element
        self.capacity = 1
        self.A = self.make_array(self.capacity)
        

    def __len__(self):
        """return the number of element store in an array"""
        return self.n
    
    def __getitem__(self, k):
        """return element at index k"""
        if not 0 <= k < self.n:
            raise IndexError('Index out of bounds')
        return self.A[k]
    
    def append(self, ele):
        """Add element to the end of the array"""
        if self.n == self.capacity:
            self._resize(2*self.capacity)
        self.A[self.n] = ele
        self.n += 1

        
    def _resize(self, new_capacity):
        """Resize the array to a new capacity"""
        B = self.make_array(new_capacity)
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
        self.capacity = new_capacity
        


    def make_array(self, capacity):
        """create new raw array with the given capactiy."""
        return (capacity * ctypes.py_object)()




dyn_array = DynamicArray()

dyn_array.append(10)
dyn_array.append(20)
dyn_array.append(30)

print(len(dyn_array))
print(dyn_array[0])
