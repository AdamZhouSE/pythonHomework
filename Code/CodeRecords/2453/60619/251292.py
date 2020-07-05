numbers = input().split(",")
target = int(input())
result = -1
if target < int(numbers[0]):
    i = len(numbers)-1
    while i > 0:
        if int(numbers[i]) == target:
            result = i
            break
        elif target > int(numbers[i]):
            break
        i -= 1
elif target > int(numbers[0]):
    i = 0
    while i <= len(numbers)-1:
        if target == int(numbers[i]):
            result = i
            break
        elif target < int(numbers[i]):
            break
        i += 1
else:
    result = 0
if result != -1:
    print(True)
else:
    print(False)