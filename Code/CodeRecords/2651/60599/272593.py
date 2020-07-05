k = int(input())
for u in range(k):
    n = int(input())
    d = 1
    sum = 0
    while n > 0:
        if (n % 2 == 1):
            if (d % 2 == 1):
                sum += 2 ** (d)
            elif (d % 2 == 0):
                sum += 2 ** (d - 2)
        d+=1
        n //= 2
    print(sum)
