line1 = input().split()
n = int(line1[0])
m = int(line1[1])
text = input()
words = []
for i in range(n - m + 1):
    word = text[i:i+m]
    if word not in words:
        words.append(word)
print(len(words))