import re;
#from itertools import *
#s = list([int(n) for n in re.findall(r"\-?\d+", input())])
for _ in range(int(input())):
    n, x, y = map(int, input().split())
    Ai = list([int(n) for n in re.findall(r"\-?\d+", input())])
    Bi = list([int(n) for n in re.findall(r"\-?\d+", input())])
    diff = list([x - y for x, y in zip(Ai, Bi)])
    index = list(range(n))
    di_zip = zip(diff, index)
    di_zip = sorted(di_zip, key=lambda q: -abs(q[0]))
    ans = 0
    diff.sort()
    for k, v in di_zip:
        if k > 0:
            if x > 0:
                x -= 1
                ans += Ai[v]
            else:
                y -= 1
                ans += Bi[v]
        else:
            if y > 0:
                y -= 1
                ans += Bi[v]
            else:
                x -= 1
                ans += Ai[v]
    print(ans)