import numpy as np

# 1-D Array or Vector
a = np.array([1, 2, 3, 4])
print(a)
print(type(a)) # Type
print(a.shape) # Shape
print(a.ndim) # Diemention
print(a.dtype) # Data TYpe

# 2-D Array
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print(type(b)) # Type
print(b.shape) # Shape
print(b.ndim) # Diemention
print(b.dtype) # Data TYpe

# 3-D Array
c = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print(c)
print(type(c)) # Type
print(c.shape) # Shape
print(c.ndim) # Diemention
print(c.dtype) # Data TYpe

# 3-D Array
d = np.array([[[1.0, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]], 
                
                [[10, 11, 12], 
                [13, 14, 15], 
                [16, 17, 18]]])
print(d)
print(type(d)) # Type
print(d.shape) # Shape
print(d.ndim) # Diemention
print(d.dtype) # Data TYpe
print(d.size) # Determine how many elements are there in an array
print(d.nbytes) # Determine how many bytes consumed by an array

# How to Create Array
x = np.array([1, 2, 3], dtype='int')
print(x)

y = np.zeros((3,3), dtype='int')
print(y)

z = np.ones((3,3), dtype='int')
print(z)

p = np.full((3,3), 5, dtype='int')
print(p)
