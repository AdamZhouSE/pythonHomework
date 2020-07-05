num = input().split(",")
numbers = [int(i) for i in num]
if numbers[0] < numbers[len(numbers)-1]:
    print(numbers[0])
else:
    i = len(numbers) - 1
    while numbers[i-1] < numbers [i]:
        i -= 1
    print(numbers[i])