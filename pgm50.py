#Extract all odd numbers from an array
import numpy as np
array=np.array([[1,2,3],[4,5,6],[7,8,9]])
oddNum=array%2==0
print("Original Array:")
print(array)
print("Odd Number Array")
print(array[oddNum])