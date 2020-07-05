t = int(input())
for index in range(t):
    length = int(input())
    numbers = input().split(" ")
    leftMax = [0]
    rightMin = []
    for i in range(length):
        rightMin.append(0)
    rightMin.append(999999)
    for i in range(1, length+1):
        leftMax.append(max(leftMax[i-1], int(numbers[i-1])))
    j = length - 1
    while j >= 0:
        rightMin[j] = min(rightMin[j+1], int(numbers[j]))
        j -= 1
    findTarget = False
    for i in range(1, length-1):
        if leftMax[i] <= int(numbers[i]) <= rightMin[i+1]:
            print(numbers[i])
            findTarget = True
            break
    if not findTarget:
        print(-1)