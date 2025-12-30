import math

def triangle(base, height):
    return 0.5 * base * height
def hexagon(side):
    height = (math.sqrt(3) / 2) * side
    onetriangle = triangle(side, height)
    return 6 * onetriangle
a = float(input("side"))
area = hexagon(a)
print(area)

