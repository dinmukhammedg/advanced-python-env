def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def lcm(a, b):
    return (a * b) // gcd(a, b)
A = int(input("num1"))
B = int(input("num2"))
result_gcd = gcd(A, B)
result_lcm = lcm(A, B)
print(result_gcd)
print(result_lcm)