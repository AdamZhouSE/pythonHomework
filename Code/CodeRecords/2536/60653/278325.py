import re
from collections import defaultdict
s = list([n for n in re.findall(r"[A-Z]+", input())])
t = []
tmp = []
a = 0
for i in s:
    if a==0:
        tmp.append(i)
        a = 1
    else:
        a = 0
        tmp.append(i)
        t.append(tmp)
        tmp = []
graph = defaultdict(list)
airports = defaultdict(int)
res = []
for x, y in t:
    graph[x].append(y)
    airports[x + y] += 1
#        print(graph)

def dfs(i, tmp, airports):
    global res
    if len(tmp) == len(t) + 1:
        res = tmp
        return
    for j in sorted(graph[i]):
        if airports[i + j] > 0 and not res:
            airports[i + j] -= 1
            dfs(j, tmp + [j], airports)
            airports[i + j] += 1
dfs("JFK", ["JFK"], airports)
print(res)