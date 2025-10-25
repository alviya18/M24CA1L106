def rectangle(l, b):
    area = l * b
    perimeter = 2 * (l + b)
    return print(f"area : ", area, "\nperimeter : ", perimeter)


def circle(r):
    area = round(3.14 * r * r,2)
    perimeter = round(2 * 3.14 * r,2)
    return print(f"area : ", area, "\nperimeter : ", perimeter)
