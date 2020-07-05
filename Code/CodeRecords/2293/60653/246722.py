import re;
from itertools import *
#s = list([int(n) for n in re.findall(r"\-?\d+", input())])
m = int(input())
for i in range(0, m):
    n = int(input())
    s = list([int(n) for n in re.findall(r"\-?\d+", input())])
    k = int(input())
    s.sort()
    print(s[k-1])