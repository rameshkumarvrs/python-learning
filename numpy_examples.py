import numpy as np

ary = np.array([1,2,3,4])

twod_ary = np.array([
	[1,2,3],
	[4,5,6]
	])


print(twod_ary)

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