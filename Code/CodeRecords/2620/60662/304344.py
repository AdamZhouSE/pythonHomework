import math

t = int(input())
i = t
res = list()

while i > 0:
    ans = 0
    n = int(input())
    i = i - 1
    while n > 0:
        ans = ans + pow(n, 5)
        n = n - 1
    res.append(ans)

while i < t:
    print(res[i])
    i = i + 1
