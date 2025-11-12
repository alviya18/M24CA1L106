#Create a class Complex with private attributes real and imaginary parts. Overload '>=' operator to find the greatest number
import math
class Complex:
    def __init__(self,real,imag):
        self.__real=real
        self.__imag=imag

    def __ge__(self,other):
        magnitude1=math.sqrt(pow(self.__real,2)+pow(self.__imag,2))
        magnitude2=math.sqrt(pow(other.__real,2)+pow(other.__imag,2))
        return magnitude1>=magnitude2

    def __eq__(self,other):
        magnitude1 = math.sqrt(pow(self.__real, 2) + pow(self.__imag, 2))
        magnitude2 = math.sqrt(pow(other.__real, 2) + pow(other.__imag, 2))
        return magnitude1 == magnitude2

    def __str__(self):
        return f"{self.__real} + {self.__imag}i"

num1=Complex(2,6)
num2=Complex(3,9)
print(num1)
print(num2)
if num1>=num2:
    if num1==num2:
        print("Both are equal")
    else:
        print(num1, "is greater")
else:
    print(num2, "is greater")
