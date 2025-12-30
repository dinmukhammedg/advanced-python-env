import math

def rectangle(l, w):
    return l * w
def square(s):
    return s * s
def triangle(b, h):
    return 0.5 * b * h
def circle(r):
    return math.pi * r * r
def trapezoid(a, b, h):
    return 0.5 * (a + b) * h
print("1 rectangle")
print("2 square")
print("3 triangle")
print("4 circle")
print("5 trapezoid")
choice = int(input("enter number"))
if choice == 1:
    l = float(input("enter length"))
    w = float(input("enter width"))
    print(f"rectangle area: {rectangle(l, w)}")
elif choice == 2:
    s = float(input("enter side"))
    print(f"square: {square(s)}")
elif choice == 3:
    b = float(input("enter base"))
    h = float(input("enter height"))
    print(f"triangle: {triangle(b, h)}")
elif choice == 4:
    r = float(input("enter radius"))
    print(f"circle area: {circle(r)}")
elif choice == 5:
    a = float(input("enter first parallel side"))
    b = float(input("enter second parallel side"))
    h = float(input("enter height"))
    print(f"trapezoid area: {trapezoid(a, b, h)}")
else:
    print("invalid number")