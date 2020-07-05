n = int(input())
initial = []
for i in range(n):
    initial.append([int(x) for x in input().split()])
ans = []
for i in range(n):
    now = initial[:i]+initial[i+1:]
    res = set()
    for j in now:
        l,r = j
        for m in range(l,r):
            res.add(m)
    ans.append(len(res))
print(str(max(ans)),end="")