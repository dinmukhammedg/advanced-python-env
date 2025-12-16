num1 = int(input("First number: "))
operator = input("Operation: ")
num2 = int(input("Second number: "))

if operator == "+":
    plus = num1 + num2
    print(plus)
elif operator == "-":
    minus = num1-num2
    print(minus)
elif operator == "*":
    mult = num1*num2
    print(mult)
elif operator == "/":
    if num2 == 0:
        print("Cant divide by zero!")
    else:
        div = num1/num2
        print(div)
else:
    print("Invalid operator")

    