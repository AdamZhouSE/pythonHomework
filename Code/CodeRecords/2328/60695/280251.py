import itertools

a = input().split(",")
a = list(map(int, a))
a = sorted(a)
res = [""]
for a in itertools.permutations(a):
    if a[:2] > (2, 3) or a[2:] > (5, 9):
        continue
    res.append('%d%d:%d%d' % a)
print(max(res))