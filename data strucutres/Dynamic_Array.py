import ctypes

class DynamicArray(object):
    
    def public(self):
        print("""
        For any dynamic array A,
        
        A=DynamicArray()
        
        A.capacity : prints the capacity of the dynamic array
        A.n : prints the number of elements in the array
        A.__len__() : returns the number of elements in the array
        A.__getitem__(k) : gets the element at kth index
        A[k] : an altenate way to get the element at the kth index
        A.append(n) :  appends the element n to the array
        A.resize(new_capacity) : resizes the array to be one of the required capacity
        self.make_array(new_cap) : used to initailize a fixed capacity/size array
        """)        
    
    def __init__(self):
        self.n=0
        self.capacity=1
        self.A=self.make_array(self.capacity)
    
    def __len__(self):
        return self.n
    
    def __getitem__(self,k):
        if not 0 <= k < self.n:
            return IndexError('k index is out of bounds')
        
        return self.A[k]
    
    def append(self,ele):
        if self.n == self.capacity:
            self._resize(2*self.capacity)
        
        self.A[self.n] = ele
        self.n += 1
        
    def _resize(self,new_cap):
        B = self.make_array(new_cap)
        for k in range(self.n):
            B[k]=self.A[k]
        self.A=B
        self.capacity=new_cap
    
    def make_array(self,new_cap):
        return(new_cap*ctypes.py_object)()
     
