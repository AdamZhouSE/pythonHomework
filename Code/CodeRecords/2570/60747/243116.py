import re
from bisect import bisect_left
num=int(input())
s=[]
envelopes=[]
for i in range(num):
    s=input().split(",")
    for j in range(len(s)):
        s[j]=int(s[j])
    envelopes.append(s)
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