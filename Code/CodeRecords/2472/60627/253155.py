# 10
from collections import Counter
n = int(input())
for i in range(n):
    input()
    s = input()
    r = Counter(list(s))
    ok = False
    for i in list(r):
        if r[i] == 1:
            print(i)
            ok = True
            break
    if not ok:
        print(-1)