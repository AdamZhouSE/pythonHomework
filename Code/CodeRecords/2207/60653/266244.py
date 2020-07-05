from itertools import *
m = int(input())
for v in range(0, m):
    a, b = map(int, input().split())
    #num = int(input())
    ls = list(int(n) for n in range(1, a+1))
    flag = 0
    for q in combinations(ls, b):
        if sum(q) == a:
            flag = 1
    print(flag)