import math

def areaheron(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
def quadrilateral(a, b, c, d, diagonal):
    area1 = areaheron(a, b, diagonal)
    area2 = areaheron(c, d, diagonal)
    return area1 + area2
side1 = float(input("side 1"))
side2 = float(input("side 2"))
side3 = float(input("side 3"))
side4 = float(input("side 4"))
diag = float(input("diagonal"))
area = quadrilateral(side1, side2, side3, side4, diag)
print(area)