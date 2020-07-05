t = int(input())
for index in range(t):
    length = int(input())
    numbers = input().split(" ")
    for i in range(0, length, 2):
        if i+1 <= length-1:
            temp = numbers[i+1]
            numbers[i+1] = numbers[i]
            numbers[i] = temp
    print(*numbers)
