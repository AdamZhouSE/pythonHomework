t = int(input())
for index in range(t):
    length = int(input())
    numbers = input().split(" ")
    sum = 0
    for i in range(length-1):
        sum += int(numbers[i])
    result = int((length+1)*length/2) - sum
    print(result)