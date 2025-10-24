def cuboid(l, b, h):
    area = 2 * (l*b + b*h + l*h)
    perimeter = 4 * (l + b + h)
    return print(f"surface_area : ", area, "\nperimeter : " ,perimeter)


def sphere(r):
    area = round(4 * 3.14 * r * r,2)
    return print(f"surface_area : ", area)

