t = int(input())
while t:
    n = int(input())
    if n == 0 or n == 1:
        print(n)
    elif (n and not (n & (n - 1))):
        print(1)
    else:
        c = 0
        while n:
            if (n % 2 == 1):
                c += 1
            n //= 2
        print(c)
    t -= 1
    