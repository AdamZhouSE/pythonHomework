t = int(input())
for index in range(t):
    l = input().split(" ")
    len = int(l[0])
    k = int(l[1])
    numbers = input().split(" ")
    startPoint = 0
    while startPoint < len:
        endPoint = min(startPoint+k, len)
        while endPoint > startPoint + 1:
            for i in range(startPoint, endPoint-1):
                if int(numbers[i]) < int(numbers[i+1]):
                    temp = numbers[i+1]
                    numbers[i+1] = numbers[i]
                    numbers[i] = temp
            endPoint -=1
        startPoint += k
    for i in range(len):
        if i == len-1:
            print(numbers[i]，end=" ")
        else:
            print(numbers[i], end=" ")
