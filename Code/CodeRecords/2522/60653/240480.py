import re;
#from itertools import *
s = list([int(n) for n in re.findall(r"\-?\d+", input())])
print(s)
t = list([int(n) for n in re.findall(r"\-?\d+", input())])
print(t)
ans = []
for i in t:
    while i in s:
        ans.append(i)
        s.remove(i)
s.sort()
for i in s:
    ans.append(i)
print(ans)