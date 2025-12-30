def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def subtract(a, b, c, d):
    numerator = a * d - c * b
    denominator = b * d
    sign = 1
    if numerator < 0:
        sign = -1
        numerator = abs(numerator)
    common = gcd(numerator, denominator)
    numerator = (numerator // common) * sign
    denominator = denominator // common
    return numerator, denominator
A = int(input("a"))
B = int(input("b"))
print("second")
C = int(input("c"))
D = int(input("d"))
num, den = subtract(A, B, C, D)
print(f"({A}/{B}) - ({C}/{D}) = {num}/{den}")