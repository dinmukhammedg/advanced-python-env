def calculator(arr):
    total = sum(arr)
    mean = total / len(arr)
    return total, mean
print("enter array 1")
array1 = list(map(int, input().split()))[:15]
print("enter array 2")
array2 = list(map(int, input().split()))[:15]
print("enter array 3")
array3 = list(map(int, input().split()))[:15]
sum1, mean1 = calculator(array1)
sum2, mean2 = calculator(array2)
sum3, mean3 = calculator(array3)
print(f"\narray 1: {array1}")
print(f"sum = {sum1}, mean = {mean1}")
print(f"\narray 2: {array2}")
print(f"Sum = {sum2}, mean = {mean2}")
print(f"\narray 3: {array3}")
print(f"sum = {sum3}, mean = {mean3}")