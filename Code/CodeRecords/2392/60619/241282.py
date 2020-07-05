t = int(input())
for index in range(t):
    li = input().split(" ")
    length = int(li[0])
    target = int(li[1])
    numbers = input().split(" ")
    canFind = False
    for i in range(length-1):
        for j in range(i+1, length):
            if int(numbers[i])*int(numbers[j]) == target:
                canFind = True
                break
        if canFind:
            break
    if canFind:
        print("Yes")
    else:
        print("No")
