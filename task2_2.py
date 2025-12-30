def rectangle(side1, side2):
    return side1 * side2
for i in range(1, 4):
    print(f"\nrectangle {i}:")
    side1 = float(input("side1"))
    side2 = float(input("side2"))
    area = rectangle(side1, side2)
    print(f"area {i} = {area}")