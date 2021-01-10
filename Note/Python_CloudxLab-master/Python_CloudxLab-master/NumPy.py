# NumPy library
# the numerical python library
# A library which is used in python for arrays and matrices

import numpy as np

# creating  a array

my_list = [1,2,4]
x = np.array(my_list)
print(x)

y = np.array([1,2,3])
print(y)


z = np.array([[12,2,3],[12,32,12]])
print(z)

p = np.arange(0,20,4)   # it will start from 0 to 20 with multiplication of 4 until 20 becomes the result
print(p)

# some more numpy functions are

print(p.reshape)

print(['a', 'b', 'c'] + [1, 2, 3])
a = ['a', 'b', 'c']
b =  [1, 2, 3]
c = a + b
print(c)
print( type(lambda x: x+1))

# creating a 6x6 matrix

array = np.array(0,35,)
print(array)