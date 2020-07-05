import re
from bisect import bisect_left

num=int(input())
s1=str(input())
d=s1.count("]")-1
s2=re.findall(r'\d+',s1)
new=[]
a=0
envelopes=[]
for v in s2:
    new.append(int(v))
    a=a+1
    if a==len(s2)/d:
        envelopes.append(new)
        a=0
        new=[]
res, n = 0, len(envelopes)

envelopes.sort(key=lambda a: (a[0], -a[1]))

mem = list()

for e in envelopes:

    index = bisect_left(mem, e[1])

    if len(mem) == index:

        mem.append(e[1])

    else:

        mem[index] = e[1]
print(len(mem))