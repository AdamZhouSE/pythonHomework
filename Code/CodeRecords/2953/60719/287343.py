def f(x, n):
    t = 0
    while not(x==n==1) and x > 0 and n > 0:
        if x > n:
            x -= n
        else:
            n -= x
        t += 1
    if x <= 0 or n <= 0:
        t = -1
    return t


num = int(input())
res = num - 1
for i in range(1, num//2+1):
    m = f(i, num)
    if m != -1:
        res = min(res, m)
print(res,end="")