t = int(input())
for index in range(t):
    li = input().split(" ")
    length = int(li[0])
    target = int(li[1])
    numbers = input().split(" ")
    currentP = 0
    differ = abs(target - int(numbers[0]))
    for i in range(1, length):
        x = abs(target - int(numbers[i]))
        if x < differ or (x == differ and int(numbers[i])>target):
            differ = x
            currentP = i
    print(numbers[currentP])