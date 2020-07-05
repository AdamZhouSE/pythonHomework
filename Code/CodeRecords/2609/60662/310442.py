t = int(input())
res = []
for i in range(t):
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    temp = len(s) - 1
    new = []
    for j in s:
        if s.count(j)==1 and j not in new:
            new.append(j)
    if k > len(new):
        res.append(-1)
    else:
        res.append(new[k-1])
for i in res:
    print(i)
