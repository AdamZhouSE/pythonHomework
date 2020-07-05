import re;
from itertools import *
#s = list([int(n) for n in re.findall(r"\-?\d+", input())])
t = list([int(n) for n in re.findall(r"\-?\d+", input())])
n = t[0]
c = t[1]
s = list([int(n) for n in re.findall(r"\-?\d+", input())])
cnt = 1
for i in range(0, n-1):
    if s[i+1] - s[i] <= c:
        cnt += 1
    else:
        cnt = 1
if cnt == 1 and c == 0:
    print(0)
else:
    print(cnt)
    