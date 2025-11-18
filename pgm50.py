#Extract all odd numbers from an array
import numpy as np
array=np.array([[1,2,3],[4,5,6],[7,8,9]])
oddNum=array%2!=0
print("Original Array :")
for row in array:
    print(" ".join(f"{num:4}" for num in row))
print("Odd Number Array :")
for num in array[oddNum]:
    print(num, end=" ")