def to_octal_10_digits(number):
    if number == 0:
        return "0000000000"
    octal = ""
    n = number
    while n > 0:
        remainder = n % 8
        octal = str(remainder) + octal
        n = n // 8
    while len(octal) < 10:
        octal = "0" + octal
    return octal
number = int(input(""))
result = to_octal_10_digits(number)
print(result)