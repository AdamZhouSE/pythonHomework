from collections import defaultdict
list1 = input()[3:-3].split("\"],[\"")
list1 = [i.split("\",\"") for i in list1]
list1.sort()
res = []
g = defaultdict(list)

for i in range(len(list1) - 1,-1,-1):
    g[list1[i][0]].append(list1[i][1])


def dfs(x):
    while g[x]:
        r = g[x].pop()
        dfs(r)
    res.append(x)


dfs("JFK")
res.reverse()
print(res)
