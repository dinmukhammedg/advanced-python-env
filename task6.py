def all_eq(lst):
    max_length = 0
    
    for s in lst:
        if len(s) > max_length:
            max_length = len(s)
    result = []
    for s in lst:
        current_length = len(s)
        underscores_needed = max_length - current_length
        new_string = s
        for i in range(underscores_needed):
            new_string = new_string + "_"
        result.append(new_string)
    return result
test_list = ["apple", "hi", "banana", "cat"]
new_list = all_eq(test_list)
for s in new_list:
    print(s)