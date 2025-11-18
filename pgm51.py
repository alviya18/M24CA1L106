# Demonstrate slicing operations on 2D and 3D arrays
import numpy as n

array2D = n.array([[1,2,3],[4,5,6],[7,8,9]])
array3D = n.array([[[1,2], [3,4]],[[5,6],[7,8]]])

print("2D Array:")
for row in array2D:
    print(" ".join(f"{num:4}" for num in row))

print("column1 of 2D Array:")
for num in array2D[:, 1]:
    print(num)

print("row1 of 2D Array:")
for num in array2D[1, :]:
    print(num, end=" ")
print()

print("\n3D Array:")
for matrix in array3D:
    for row in matrix:
        print(" ".join(f"{num:4}" for num in row))
    print()

print("matrix0 of 3D Array:")
for row in array3D[0]:
    print(" ".join(f"{num:4}" for num in row))

print("row1 of matrices in 3D Array:")
for row in array3D[:, 1, :]:
    print(" ".join(f"{num:4}" for num in row))

print("column1 of matrix1 in 3D Array :")
for col in array3D[1:, :, 1]:
    for num in array3D[1, :, 1]:
        print(num)
