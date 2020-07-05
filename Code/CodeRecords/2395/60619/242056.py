t = int(input())
for index in range(t):
    length = int(input())
    numbers = input().split(" ")
    for i in range(length-1):
        if int(numbers[i]) != 0 and int(numbers[i]) == int(numbers[i+1]):
            numbers[i] = str(2*int(numbers[i]))
            numbers[i+1] = "0"
    newNum = []
    for i in range(length):
        if int(numbers[i]) != 0:
            newNum.append(numbers[i])
    while len(newNum) < length:
        newNum.append("0")
    print(*newNum)