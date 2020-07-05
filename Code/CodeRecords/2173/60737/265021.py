t = int(input())
while t:
    n = int(input())
    sum = 0
    while n:
        sum += n*n
        n -= 1
    print(sum)
    t -= 1
