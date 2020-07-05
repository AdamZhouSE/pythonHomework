import re;
from itertools import *
s = input()
t = input()
sa = [0]*26
sA = [0]*26
ta = [0]*26
tA = [0]*26
sa1 = re.findall(r"[a-z]", s)
sA1 = re.findall(r"[A-Z]", s)
ta1 = re.findall(r"[a-z]", t)
tA1 = re.findall(r"[A-Z]", t)
for i in sa1:
    sa[ord(i)-ord('a')] += 1
for i in sA1:
    sA[ord(i)-ord('a')] += 1
for i in ta1:
    ta[ord(i)-ord('a')] += 1
for i in tA1:
    tA[ord(i)-ord('a')] += 1
flag = True
for i in range(0, 26):
    if sa[i] < ta[i] or sA[i] < tA[i]:
        flag = False
        break
if flag:
    print("YES", end='')
else:
    print("NO", end='')