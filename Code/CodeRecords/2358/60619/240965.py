t = int(input())
for index in range(t):
    l = input().split(" ")
    length = int(l[0])
    k = int(l[1])
    numbers = input().split(" ")
    i = 1
    while i <= k:
        for j in range(length-i):
            if int(numbers[j]) > int(numbers[j+1]):
                temp = numbers[j+1]
                numbers[j+1] = numbers[j]
                numbers[j] = temp
        i += 1
    for k in range(1, k+1):
        print(numbers[length-k], end=" ")
    print()