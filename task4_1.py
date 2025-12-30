def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def divide(a, b, c, d):
    numerator = a * d
    denominator = b * c
    common = gcd(numerator, denominator)
    numerator = numerator // common
    denominator = denominator // common
    return numerator, denominator
A = int(input("a"))
B = int(input("b"))
C = int(input("c"))
D = int(input("d"))
num, den = divide(A, B, C, D)
print(f"({A}/{B})/({C}/{D})={num}/{den}")