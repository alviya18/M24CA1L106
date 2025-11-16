#Demonstrate sum(), cumsum(), max() and min() axis wise on a 2D array
import numpy as n
array=n.array([[1,2],[3,4],[5,6],[7,8]])
print("Original Array\n",array)
print("array with cummulative col sum :\n",n.cumsum(array,axis=1))
print("array with cummulative row sum :\n",n.cumsum(array,axis=0))
print("array with maximum col value :\n",n.max(array,axis=1))
print("array with maximum row value :\n",n.max(array,axis=0))
print("array with minimum col value :\n",n.min(array,axis=1))
print("array with minimum row value :\n",n.min(array,axis=0))
