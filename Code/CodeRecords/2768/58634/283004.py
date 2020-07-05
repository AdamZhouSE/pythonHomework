t = int(input())
for i in range(t):
    a,b,m = map(int,input().split(" "))
    res = 0
    x = 0
    for _ in range(a,b+1):
        if _ % m == 0:
            x = _
    for j in range(x,b+1,m):
        res += 1
    print(res)
        