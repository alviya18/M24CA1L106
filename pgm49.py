#Write a program to perform element-wise trigonometric functions (sin, cos, tan) on an array
import numpy as np

# Input array in degrees
array = np.array([[0, 15, 30], [45, 60, 90]])
print("Original array (degrees):")
print(array)

# Convert degrees to radians
radians = np.deg2rad(array)

# Element-wise trigonometric functions
sinArray = np.sin(radians)
cosArray = np.cos(radians)
tanArray = np.tan(radians)

print("\nSine values:")
print(sinArray)
print("\nCosine values:")
print(cosArray)
print("\nTangent values:")
print(tanArray)
