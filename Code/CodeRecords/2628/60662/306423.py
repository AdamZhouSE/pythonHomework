def myArea(points):
    a = abs(points[0]*(points[3]-points[5])+points[2]*(points[5]-points[1])+points[4]*(points[1]-points[3]))/2
    return a


n = int(input())
res = []
for i in range(n):
    x = []
    y = []
    ans = 0
    for j in range(3):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    s = myArea([x[0], y[0], x[1], y[1], x[2], y[2]])
    for m in range(min(x), max(x)):
        for p in range(min(y), max(y)):
            s1 = myArea([x[0], y[0], x[1], y[1], m, p])
            s2 = myArea([x[0],  y[0],x[2], y[2], m, p])
            s3 = myArea([x[1],  y[1],x[2], y[2], m, p])
            if s == (s1 + s2 + s3) and s1 != 0 and s2 != 0 and s3 != 0:
                ans = ans + 1
    res.append(ans)
for i in res:
    print(i)
