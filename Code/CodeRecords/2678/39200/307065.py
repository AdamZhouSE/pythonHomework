from math import log
t = int(input())
for x in range(t):
    n = int(input())
    if (log(n, 2) + 1).is_integer():
        print(int(log(n, 2) + 1))
    else:
        print(-1)
