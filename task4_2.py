def inside(px, py, xa, yb, r):
    distance2 = (px - xa)**2 + (py - yb)**2
    if distance2 < r**2:
        return True
    else:
        return False
xa = float(input("center x"))
yb = float(input("center y"))
R = float(input("radius"))
print("P")
p1 = float(input("p1"))
p2 = float(input("p2"))
print("F")
f1 = float(input("f1"))
f2 = float(input("f2"))
print("L")
l1 = float(input("l1"))
l2 = float(input("l2"))
count = 0
if inside(p1, p2, xa, yb, R):
    count += 1
    print("P is inside")
if inside(f1, f2, xa, yb, R):
    count += 1
    print("F is inside")
if inside(l1, l2, xa, yb, R):
    count += 1
    print("L is inside")
print(f"points inside: {count}")