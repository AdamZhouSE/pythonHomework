def dSum(n):
    s = 0
    for i in range(1, n + 1):
        if n % i == 0:
            s += i
    return s

T = int(input())
for t in range(T):
    x = int(input())
    if dSum(x) < 2 * x: print(1)
    else: print(0)