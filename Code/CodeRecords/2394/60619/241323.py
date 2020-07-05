t = int(input())
for index in range(t):
    length = int(input())
    numbers = input().split(" ")
    newNum = []
    for i in range(length):
        if int(numbers[i]) != 0:
            newNum.append(numbers[i])
    while len(newNum) < length:
        newNum.append("0")
    print(*newNum,end=)
