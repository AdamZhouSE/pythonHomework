import re;
from itertools import *
#s = list([int(n) for n in re.findall(r"\-?\d+", input())])
n = int(input())
s = list([int(n) for n in re.findall(r"\-?\d+", input())])
t = []
k = 0
a = 0
while pow(a, 2) <= pow(10, 6):
    k = pow(a, 2)
    a += 1
    t.append(k)
b = []
for i in s:
    if t.count(i) == 0 or i < 0:
        b.append(i)
print(max(b))
