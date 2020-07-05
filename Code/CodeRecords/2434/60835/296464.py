n, m, c = map(int, input().split())
a = list(map(int, input().split()))
res = []
for x in range(n - m + 1):
    jud = True
    for y in range(x + 1, x + m):
        #print(a[x] - a[y])
        if a[x] - a[y] > c or a[x] - a[y] < -c:
            jud = False
            break
    if jud:
        res.append(x + 1)
if len(res) == 0:
    print("NONE")
else:
    for x in res:
        print(x)