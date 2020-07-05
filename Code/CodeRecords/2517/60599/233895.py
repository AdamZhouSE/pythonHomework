
A=list(map(int, input().split(',')))
B=list(map(int, input().split(',')))
C=list(map(int, input().split(',')))
D=list(map(int, input().split(',')))

from collections import defaultdict
map1 = defaultdict(int)
res = 0
for a in A:
    for b in B:
        t = a + b
        map1[t] += 1
#用defaultdict优化
for c in C:
    for d in D:
        t = - c - d
        res += map1[t]
print(res)
