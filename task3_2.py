def sortword(word):
    return ''.join(sorted(word))
def sortstring(text):
    words = text.split()
    sorted_words = []
    for word in words:
        sorted_words.append(sortword(word))
    return ' '.join(sorted_words)
istring = input("input")
result = sortstring(istring)
print(result)