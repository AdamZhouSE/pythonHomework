import re;
from itertools import *
#s = list([int(n) for n in re.findall(r"\-?\d+", input())])
boy = int(input())
b = list([int(n) for n in re.findall(r"\-?\d+", input())])
b.sort()
girl = int(input())
g = list([int(n) for n in re.findall(r"\-?\d+", input())])
g.sort()
ans = 0
i = 0
j = 0
while i < boy and j < girl:
    if abs(b[i] - g[j]) <= 1:
        i += 1
        j += 1
        ans += 1
    elif b[i] > g[j]:
        j += 1
    else:
        i += 1
print(ans)