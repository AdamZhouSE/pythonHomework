# 10
from collections import Counter
n = int(input())
for i in range(n):
    input()
    s = input()
    r = Counter(list(s))
    for i in list(r):
        if r[i] == 1:
            print(i)
            break