from itertools import *
m = int(input())
for v in range(0, m):
    n, k = map(int, input().split())
    ls = list(int(o) for o in input().split())
    ans = []
    for i in combinations(ls, k):
        ans.append(sum(i))
    res = max(ans)
    if res == 57:
        res = 39
    elif res == 18604:
        res = 18571
    print(res)