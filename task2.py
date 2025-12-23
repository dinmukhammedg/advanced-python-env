a = input()
b = input()
n = len(b)
cyclic_shifts = []
for k in range(n):
    shift = b[k:] + b[:k]
    cyclic_shifts.append(shift)
count = 0
for i in range(len(a) - n + 1):
    substring = a[i:i+n]

    for shift in cyclic_shifts:
        if substring == shift:
            count = count + 1
            break
print(count)