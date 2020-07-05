#18
T = int(input())
for i in range(0,T):
    n = int(input())
    count = 0
    while n != 0:
        if n % 2 == 0:
            n = n//2
            count += 1
        else:
            n -= 1
            count += 1
    print(count)