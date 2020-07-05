import itertools
A=input().split(",")
A=list(int(a) for a in A)
res = [""]
for a in itertools.permutations(A):
    if a[:2] > (2, 3) or a[2:] > (5, 9):
        continue
    res.append('%d%d:%d%d' % a)
print(max(res))