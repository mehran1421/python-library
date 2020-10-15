import numpy as np

#Create a numpy array
a=[1,2,3,4,5,6,7,8,9]
a_arr=np.array(a)
print(type(a_arr))
#<class 'numpy.ndarray'>
print(a)
#[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a_arr)
#[1 2 3 4 5 6 7 8 9]
print("==========================================")

a=[[1,2,3],[4,5,6],[7,8,9]]
a_arr=np.array(a)
print(a_arr)
#[[1 2 3]
 # [4 5 6]
 # [7 8 9]]
print(a_arr.tolist())
#[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("==========================================")

#Specify the datatype
#float, int , bool , str, objects
a_arr=np.array(a,dtype="float")
print(a_arr)
# [[1. 2. 3.]
#  [4. 5. 6.]
#  [7. 8. 9.]]
print("==========================================")

a_arr=a_arr.astype('int')
print(a_arr)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
print("==========================================")
#Operations
print(a_arr*2)
# [[ 2  4  6]
#  [ 8 10 12]
#  [14 16 18]]
print(a_arr+a_arr)
# [[ 2  4  6]
#  [ 8 10 12]
#  [14 16 18]]

print("==========================================")
#Inspect the size and shape
print("shape: ",a_arr.shape)
print("datatype: ",a_arr.dtype)
print("size: ",a_arr.size)
print("dimensions: ",a_arr.ndim)
# shape:  (3, 3)
# datatype:  int32
# size:  9
# dimensions:  2

print("========================================")
#Condition over an array
print(a_arr>7)
# [[False False False]
#  [False False False]
#  [False  True  True]]
print(a_arr[a_arr>7])
# [8 9]


print("========================================")
#Reverse an array
print(a_arr[::-1])
# [[7 8 9]
#  [4 5 6]
#  [1 2 3]]
print(a_arr[::-1,::-1])
# [[9 8 7]
#  [6 5 4]
#  [3 2 1]]
print("========================================")

#Compute min max mean
print("min",a_arr.min())
print("max",a_arr.max())
print("mean",a_arr.mean())
# min 1
# max 9
# mean 5.0
print("========================================")
#Create a new array from an existing array
#wrong
b_arr=a_arr
b_arr[0][0]=11
print(a_arr)
# [[11  2  3]
#  [ 4  5  6]
#  [ 7  8  9]]
#corect
b_arr=a_arr.copy()
b_arr[0][0]=12
print(a_arr)
# [[11  2  3]
#  [ 4  5  6]
#  [ 7  8  9]]

print("========================================")
#Reshaping
b_arr=b_arr.reshape(1,9)
print(b_arr)
# [[12  2  3  4  5  6  7  8  9]]
print("========================================")
#Flattening
b_arr=a_arr.copy()
print(b_arr)
# [[11  2  3]
#  [ 4  5  6]
#  [ 7  8  9]]
print(b_arr.flatten())

# [11  2  3  4  5  6  7  8  9]
print("========================================")
#arange() method
print(np.arange(10))
# [0 1 2 3 4 5 6 7 8 9]
print(np.arange(10,20))
# [10 11 12 13 14 15 16 17 18 19]
print(np.arange(20,30,5))
# [20 25]
print("========================================")
#Create array items between two number
print(np.linspace(start=1,stop=1000,num=25,dtype=int))
# [   1   42   84  125  167  209  250  292  334  375  417  458  500  542
#   583  625  667  708  750  791  833  875  916  958 1000]
print("========================================")
#Generate random numbers
print(np.random.rand(1,5))
# [[0.89012267 0.16970996 0.88409339 0.30332125 0.764087  ]]
print(np.random.randint(0,5,size=[1,5]))
# [[4 3 4 3 0]]
print(np.random.choice(['G','S','B'],size=1,p=[0.1,.3,0.6]))
# ['S']

