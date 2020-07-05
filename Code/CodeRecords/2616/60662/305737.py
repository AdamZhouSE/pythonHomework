n = int(input())
res = list()
for f in range(0, n):
    a, b = list(map(int, input().split()))
    if b*(b+1)>2*a:
        res.append(0)
    else:
        res.append(1)

for d in res:
    print(d)
