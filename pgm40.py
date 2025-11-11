#Create a class Rectangle with private attributes length and width. Overload < operator to compare the area of two rectangles.
class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __lt__(self, other):
        return self.area() < other.area()

    def __str__(self,other=None):
        if other :
            return  f"Rectangle with width={self.__width} and height={self.__height} has greater area" if self.area() > other.area() else f"Rectangle with width={other.__width} and height={other.__height} has greater area"
        else:
            return f"Area of rectangle with l:{self.__height} , b:{self.__width} = {self.area()}"

r1 = Rectangle(10, 5)
r2 = Rectangle(8, 9)
print(r1)
print(r2)
if r1 < r2:
    print("r1 has smaller area")
else:
    print("r2 has smaller area")
