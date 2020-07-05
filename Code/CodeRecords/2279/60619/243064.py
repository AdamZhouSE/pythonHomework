t = int(input())
for index in range(t):
    li = input().split(" ")
    length = int(li[0])
    target = int(li[1])
    numbers = input().split(" ")
    canFind = False
    position = []
    for i in range(length):
        sum = int(numbers[i])
        for j in range(i+1, length):
            sum += int(numbers[j])
            if sum == target:
                canFind = True
                position.append(i+1)
                position.append(j+1)
                break
        if canFind:
            break
    if canFind:
        print(*position)
    else:
        print(-1)