import collections
source=list(input())
pairs=list(eval(input()))
fathers= list(range(len(source)))
def findfather(x):
    if x != fathers[x]:
        fathers[x] = findfather(fathers[x])
    return fathers[x]


for i, j in pairs:
    fx, fy = findfather(i), findfather(j)
    if fx != fy:
        fathers[fx] = fy

mem = collections.defaultdict(list)
for i, v in enumerate(fathers):
    mem[findfather(v)].append(source[i])
for k in mem:
    mem[k].sort(reverse=True)

results = []
for i in range(len(source)):
    results.append(mem[findfather(i)].pop())
print( "".join(results))