import numpy as np

#arr = np.array([[1, 2, 3] , [4, 5,6]])
#print(np.sum(arr))  # Output: (2, 2, 3)
#print(np.mean(arr))  # Output: 6
#print(np.min(arr))  # Output: 3
#print(arr.reshape(6))  # Output: [[1 2 3] [4 5 6]]
#print(arr[::5])
#print(arr.flatten())  # Output: [1 2 3 4 5 6]
#print(arr)
#print(arr.ravel())
#print(arr)
"""



#vstack syntax((arr1, arr2))
#hstack syntax((arr1, arr2))
arr1=np.array([[1, 2, 3] , [4, 5,6]])
arr2=np.array([[7, 8, 9] , [10, 11,12]])
arr3=np.vstack((arr1, arr2)) 
print(arr3)
arr4=np.hstack((arr1, arr2))
print(arr4)
arr5=np.dstack((arr1, arr2))
print(arr5)



"""

'''


arr1=np.array([[1, 2, 3] , [4, 5,6]])
arr2=np.array([[7, 8, 9] , [10, 11,12]])
print(np.split(arr1,2,axis=0)) 
print(np.split(arr1,3,axis=1))  
print(np.split(arr1,2, axis=0))  
print(np.split(arr1,3, axis=1))  
print(np.hsplit(arr1, 3)) 
print(np.vsplit(arr1, 2)) 


'''