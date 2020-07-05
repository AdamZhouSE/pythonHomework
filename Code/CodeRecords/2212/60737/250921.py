t = int(input())
while t:
    n = int(input())
    d = []
    for i in range(1, n+1):
        s = n // i
        if s*i == n:
            d.append(i)
    if sum(d) > 2*n:
        print(0)
    else:
        print(1)
    t -= 1
    