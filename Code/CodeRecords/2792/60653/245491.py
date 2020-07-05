import re;
from itertools import *
#s = list([int(n) for n in re.findall(r"\-?\d+", input())])
n = int(input())
s = list([int(n) for n in re.findall(r"\-?\d+", input())])
cnt = 0
t = []
k = 1
for i in s:
    if i == 1:
        cnt += 1
        t.append(k)
        k = 1
    else:
        k += 1
t.append(k)
t.remove(t[0])
print(cnt)
print(t[0], end='')
for i in range(1, len(t)):
    print(' ', end='')
    print(t[i], end='')
print("")