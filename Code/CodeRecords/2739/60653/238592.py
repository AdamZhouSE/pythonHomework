import re;
from itertools import *
s = list([int(n) for n in re.findall(r"\d+", input())])
k = s[0]
n = s[1]
res = []
for i in combinations(range(1, 10), k):
            if sum(i) == n:
                res.append(list(i))
print(res)