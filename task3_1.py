import math

def hypotenuse(a1, a2):
    return math.sqrt(a1**2 + a2**2)
print("triangle 1")
a1 = float(input("a1"))
b1 = float(input("b1"))
print("triangle 2")
a2 = float(input("a2"))
b2 = float(input("b2"))
hyp1 = hypotenuse(a1, b1)
hyp2 = hypotenuse(a2, b2)
print(f"\nhypotenuse 1: {hyp1}")
print(f"hypotenuse 2: {hyp2}")
if hyp1 > hyp2:
    print("hyp1 is greater")
elif hyp1 < hyp2:
    print("hyp1 is smaller")
else:
    print("equal")