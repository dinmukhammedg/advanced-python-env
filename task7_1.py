def rights(a, b):
    return 0.5 * a * b
def rectangles(a, b):
    return a * b
X = float(input("side x"))
Y = float(input("side y"))
Z = float(input("side z"))
T = float(input("side t"))
triangles = rights(X, Y)
print(triangles)
total_area = rights(X, Y) + rights(Z, T)
print(total_area)