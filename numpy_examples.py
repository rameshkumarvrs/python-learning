import numpy as np

ary = np.array([1,2,3,4])

n1 = np.array([
	[1,2,3],
	[4,5,6]
	])


print(n1)

#np zeros

ze = np.zeros([3,5], dtype='int32')

print(ze)

n3 = np.ones([4,3,3], dtype='int32')

print(n3)

n4 = np.arange(0,8)

print(n4)

n5 = np.linspace(0,20,num=5, dtype='int32')

print(n5)

n6 = np.full([2,5],75)


print(n6)

n7 = np.empty([1,3], dtype='int32')

n7.fill(9)

print(n7)

n8 = np.array([1,2,3,4])

print(n8[-1])

n3[1,1,2] = 9


print(n3) 


#shape and dimentions


print(n3.ndim)

print(n6.ndim)

print(n3.shape)

print(n3.size)

n10 = np.array([1,5,3,9,8,7,5,6])

print(np.sort(n10))


n11 = np.array(
   [

    [1,5,4],
    [9,8,5]
   ]
	)



print(np.sort(n11))

n12 = n10.reshape(4,2)

print(n12)


n14 = np.arange(4)

n15 = np.arange(1,5)


print(n14)

n16 = np.concatenate((n14,n15))

print(n16)