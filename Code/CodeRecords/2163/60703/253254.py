import itertools
n = int(input())
k = int(input())
m = list(range(n))
oj = itertools.permutations(m)
resList = list(oj)
resList.sort()
res =resList[k-1]
print("".join([str(x) for x in res]))
