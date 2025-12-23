n = int(input())
valid_letters = "ABCEHKMOPTXY"
valid_digits = "0123456789"
for i in range(n):
    plate = input()
    is_valid = True
    if len(plate) != 6:
        is_valid = False
    if is_valid == True:
        if plate[0] not in valid_letters:
            is_valid = False
    if is_valid == True:
        if plate[1] not in valid_digits:
            is_valid = False
    if is_valid == True:
        if plate[2] not in valid_digits:
            is_valid = False
    if is_valid == True:
        if plate[3] not in valid_digits:
            is_valid = False
    if is_valid == True:
        if plate[4] not in valid_letters:
            is_valid = False
    if is_valid == True:
        if plate[5] not in valid_letters:
            is_valid = False
    if is_valid == True:
        print("Yes")
    else:
        print("No")