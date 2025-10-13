"""Write lambda functions, each to find area of square, rectangle and triangle. """
squareArea = lambda a: a * a
rectangleArea = lambda l,w: l * w
triangleArea = lambda b,h: round((b * h)/ 2,2)
print(f"SQUARE\nside: 4\narea: {squareArea(4)}\nRECTANGLE\nlength: 34\nwidth:17\narea: {rectangleArea(20.4,9)}\nTRIANGLE\nbase: 12\nheight: 24\narea: {triangleArea(12,24)}")