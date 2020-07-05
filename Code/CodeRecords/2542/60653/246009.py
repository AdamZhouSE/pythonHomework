import re;
from itertools import *
#s = list([int(n) for n in re.findall(r"\-?\d+", input())])
s = list([int(n) for n in re.findall(r"\-?\d+", input())])
s.sort()
ans = 0
temp = s[0]
for i in s:
    if abs(i - temp) <= 1:
        ans += 1
    else:
        break
    temp = i
if len(s) == 0:
    print(0)
else:
    print(ans)