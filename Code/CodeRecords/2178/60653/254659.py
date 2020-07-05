import re;
from itertools import *
n = int(input())
a = list([int(n) for n in re.findall(r"\-?\d+", input())])
fail = [0]*200010
fail[0] = -1
step = [0]*200010
last = 0
id = 0
tmp = list([0]*200010)
ch = [[0]*13010 for i in range(13010)]
res = []
for i in a:
    x = i
    id += 1
    np = id
    p = last
    step[np] = step[p] + 1
    last = np
    while p != -1 and ch[p][x] == 0:
        ch[p][x] = np
        p = fail[p]
    if p == -1:
        fail[np] = 0
    else:
        q = ch[p][x]
        if step[p]+1 == step[q]:
            fail[np] = q
        else:
            id += 1
            nq = id
            step[nq] = step[p] + 1
            ch[nq] = ch[q]
            fail[nq] = fail[q]
            fail[q] = fail[np] = nq
            while p != -1 and ch[p][x] == q:
                ch[p][x] = nq
                p = fail[p]
    res.append(step[np]-step[fail[np]])
#    print(step[np]-step[fail[np]])
ans = 0
for i in res:
    ans += i
    print(ans)