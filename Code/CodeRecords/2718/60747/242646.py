import re
import collections
s=input()
s1=str(input())
d=s1.count("]")-1
s2=re.findall(r'\d+',s1)
new=[]
a=0
pairs=[]
for v in s2:
    new.append(int(v))
    a=a+1
    if a==len(s2)/d:
        pairs.append(new)
        a=0
        new=[]
p = list(range(len(s)))


def find(x):
    if x != p[x]:
        p[x] = find(p[x])

    return p[x]


for i, j in pairs:

    px, py = find(i), find(j)

    if px != py:
        p[px] = py

mem = collections.defaultdict(list)

for i, v in enumerate(p):
    mem[find(v)].append(s[i])

for k in mem:
    mem[k].sort(reverse=True)

res = []

for i in range(len(s)):
    res.append(mem[find(i)].pop())
print("".join(res))