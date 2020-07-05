import itertools
n = int(input())
k = int(input())
m = list(range(1,n+1))
oj = itertools.permutations(m)
resList = list(oj)
resList.sort()
res =resList[k-1]
print("".join([str(x) for x in res]))
