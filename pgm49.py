#Write a program to perform element-wise trigonometric functions (sin, cos, tan) on an array
import numpy as np

array = np.array([[0, 15, 30], [45, 60, 90]])
print("Original array (degrees):")
for row in array:
    print(" ".join(f"{num:4}" for num in row))

radians = np.deg2rad(array)
sinArray = np.sin(radians)
cosArray = np.cos(radians)
tanArray = np.tan(radians)

print("\nSine values:")
for row in sinArray:
    print(" ".join(f"{num:6.2f}" for num in row))

print("\nCosine values:")
for row in cosArray:
    print(" ".join(f"{num:6.2f}" for num in row))

print("\nTangent values:")
for row in tanArray:
    print(" ".join(f"{num:6.2f}" for num in row))
