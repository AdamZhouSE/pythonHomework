from itertools import *
n, k = map(int, input().split(' '))
ls = []
max = 0
for i in range(0, k):
    ls.append(list(int(m) for m in input().split(' ')))
for t in range(1, n):
    for a in combinations(ls[0], t):
        flag = False
        res = []
        for i in range(1, k):
            for b in combinations(ls[i], t):
                if a == b:
                    flag = True
                    break
            if flag:
                res.append(t)
        if res.count(t) == k-1:
            max = t
print(max)