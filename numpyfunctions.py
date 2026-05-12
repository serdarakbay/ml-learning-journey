import numpy as np 
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[3,4,5],[6,7,8]])
c=np.array([10,11,12],dtype='int16')
print(a*b)
print(a.ndim)#get dimension
print(c.ndim)#
print(a.shape)#get shape
print(c.shape)#
print(a.dtype)#get type
print(c.dtype)#
print(a.itemsize)#get size
print(c.itemsize)#
print(a.nbytes)#get total size
print(c.nbytes)#
print(a[1,1])#get an element
print(a[0,:])#get a row
d=c.copy()#if you dont use .copy c and d's first element becomes 100
d[0]=100
print(c)
e=np.ones((2,3))
f=np.full((3,2),2)
g=np.matmul(e,f)
print(g)    
print([a>3])
print(a+b)
print(a*b)