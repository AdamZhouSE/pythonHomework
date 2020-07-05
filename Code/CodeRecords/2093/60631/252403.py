import itertools
n = int(input())
k = int(input())
li = []
for i in range(1,n+1):
    li.append(i)
out = []
for j in itertools.permutations(li):
    out.append(j)
lii = list(out[k-1])
a = []
for k in lii:
    a.append(str(k))
print(''.join(a))