t = int(input())

for i in range(t):
    n = int(input())
    li = []
    num = 1
    count = 1
    while n > 0:
        count2 = count
        while count2 > 0 and n > 0:
            li.append(num)
            count2 = count2 - 1
            num = num + 2
            n = n - 1
        num = num - 1
        count = count + 1
    print(*map(int,li))
    
