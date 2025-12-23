equation = input()
a = equation[0]
op = equation[1]
b = equation[2]
c = equation[4]
if a == 'x':
    b = int(b)
    c = int(c)
    if op == '+':
        x = c - b
    else:
        x = c + b
elif b == 'x':
    a = int(a)
    c = int(c)
    if op == '+':
        x = c - a
    else:
        x = a - c
else:
    a = int(a)
    b = int(b)
    if op == '+':
        x = a + b
    else:
        x = a - b
print(x)