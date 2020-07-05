t = int(input())
for k in range(t):
    a,b = [int(i) for i in input().split()]
    n = int(input())
    d = b-a
    res = a
    for i in range(n-1):
        res += d
    print(res)