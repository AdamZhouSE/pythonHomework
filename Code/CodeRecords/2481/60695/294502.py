t = int(input())
for i in range(t):
    nm = input().split(" ")
    n = int(nm[0])
    m = int(nm[1])
    a = input().split(" ")
    b = input().split(" ")
    res = []
    for i in range(n):
        if a[i] in b and a[i] not in res:
            res.append(a[i])
    for i in range(m):
        if b[i] in a and b[i] not in res:
            res.append(b[i])
    print(len(res))