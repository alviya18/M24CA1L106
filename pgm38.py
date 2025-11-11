# Create Rectangle class with attributes length and breadth and methods to find area and perimeter. Compare two Rectangle objects by their area.
class Rectangle :
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self,length,breadth):
        return length*breadth

    def perimeter(self,length,breadth):
        return 2*(length+breadth)

    def __str__(self):
        return f"Area of Rectangle with length {self.length} , breadth {self.breadth} : {self.area(self.length, self.breadth)}"

l1, b1 = map(int, input("Length & Breadth ? : ").split())
l2, b2 = map(int, input("Length & Breadth ? : ").split())

s1 = Rectangle(l1, b1)
s2 = Rectangle(l2, b2)

print(s1)
print(s2)

print(f"Rectangle with l={l1} and b={b1} have greater area" if s1.area(s1.length, s1.breadth) > s2.area(s2.length, s2.breadth) else f"Rectangle with l={l2} and b={b2} have greater area")
