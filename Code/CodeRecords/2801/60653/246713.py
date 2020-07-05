import re;
from itertools import *
#s = list([int(n) for n in re.findall(r"\-?\d+", input())])
m = int(input())
s = list([int(n) for n in re.findall(r"\-?\d+", input())])
flag = False
for k in combinations(s, 3):
    if sum(k) > 2*max(k) and k[0] - k[1] < k[2] and k[1] - k[2] < k[0] and k[0] - k[2] < k[1]:
        flag = True
        break
if flag:
    print("YES")
else:
    print("NO")