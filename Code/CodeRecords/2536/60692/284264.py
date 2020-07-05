from collections import defaultdict
i = input()
x = i.find(',')
if i[x + 1] == ' ':
    list1 = i[3:-3].split("\"], [\"")
    list1 = [j.split("\", \"") for j in list1]
else:
    list1 = i[3:-3].split("\"],[\"")
    list1 = [j.split("\",\"") for j in list1]
list1.sort()
res = []
g = defaultdict(list)
list1.reverse()
for i in range(len(list1)):
    g[list1[i][0]].append(list1[i][1])


def dfs(x):
    while g[x]:
        r = g[x].pop()
        dfs(r)
    res.append(x)


dfs("JFK")
res.reverse()
print(res)