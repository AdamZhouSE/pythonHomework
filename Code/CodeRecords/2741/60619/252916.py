num = input().replace("[", "").replace("]", "").split(",")
numbers = [int(i) for i in num]
length = len(numbers)
result = 0
currentL = 1
for i in range(length-1):
    if numbers[i] < numbers[i+1]:
        currentL += 1
    else:
        if currentL > result:
            result = currentL
        currentL = 1
print(result)