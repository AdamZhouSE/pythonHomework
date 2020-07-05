import math
n = int(input())
h = int(math.log(n, 2))
p = 2
l = set()
l.add(2)
ans = 0
for i in range(h-1, 1, -1):
    p = int(pow(n, 1/i))
    l.add(p)
for c in l:
    if n%c == 1:
        u = n*c-n+1
        t = c
        while t < u:
            t *= c
            if t == u:
                ans = c
                break
    if ans != 0:
        break
if ans != 0:
    print(ans)
else:
    print(n-1)