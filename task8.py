s1 = input()
s2 = input()
if len(s1) != len(s2):
    print("NO")
else:
    letters1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    counts1 = []
    for letter in letters1:
        count = 0
        for char in s1:
            if char == letter:
                count = count + 1
        counts1.append(count)
    counts2 = []
    for letter in letters1:
        count = 0
        for char in s2:
            if char == letter:
                count = count + 1
        counts2.append(count)
    is_anagram = True
    for i in range(26):
        if counts1[i] != counts2[i]:
            is_anagram = False
            break
    if is_anagram == True:
        print("YES")
    else:
        print("NO")