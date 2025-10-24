from graphics import circle as c,rectangle as rect
from graphics.threeDgraphics import *

r = int(input("Radius? : "))
print("CIRCLE***********")
c(r)
print("SPHERE***********")
sphere(r)
l,b,h=int(input("Length? : ")),int(input("Breadth? : ")),int(input("Height? : "))
print("RECTANGLE********")
rect(l,b)
print("CUBOID***********")
cuboid(l,b,h)



