# 10
from collections import Counter
n = int(input())
for i in range(n):
    input()
    s = input()
    r = Counter(list(s))
    print(r.values())