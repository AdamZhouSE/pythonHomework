import re
s1=str(input())
d=s1.count("]")-1
s2=re.findall(r'\d+',s1)
new=[]
a=0
stones=[]
for v in s2:
    new.append(int(v))
    a=a+1
    if a==len(s2)/d:
        stones.append(new)
        a=0
        new=[]
UF = {}


def find(x):
    if x != UF[x]:
        UF[x] = find(UF[x])

    return UF[x]


def union(x, y):
    UF.setdefault(x, x)

    UF.setdefault(y, y)

    UF[find(x)] = find(y)


for i, j in stones:
    union(i, ~j)
print(len(stones) - len({find(x) for x in UF}))