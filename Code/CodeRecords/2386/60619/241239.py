t = int(input())
for index in range(t):
    length = int(input())
    numbers = input().split(" ")
    target = int(input())
    canFind = False
    for i in range(length-3):
        for j in range(i+1, length-2):
            for k in range(j+1, length-1):
                for x in range(k+1, length):
                    if int(numbers[i]) + int(numbers[j]) + int(numbers[k]) + int(numbers[x]) == target:
                        canFind = True
                        break
                if canFind:
                    break
            if canFind:
                break
        if canFind:
            break
    if canFind:
        print(1)
    else:
        print(0)
