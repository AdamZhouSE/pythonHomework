t = int(input())
while t:
    n = int(input())
    sum = 0
    while n:
        sum += int(n * (n+1) / 2)
        n -= 1
    print(sum)
    t -= 1
    