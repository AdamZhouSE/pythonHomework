import re
def __dfs(vertex, inverse_adj, visited, res):
    if visited[vertex] == 2:
        return True
    if visited[vertex] == 1:
        return False
    visited[vertex] = 2
    for precursor in inverse_adj[vertex]:
        if __dfs(precursor, inverse_adj, visited, res):
            return True
    visited[vertex] = 1
    res.append(vertex)
    return False


n = int(input())
s = list([int(n) for n in re.findall(r"\-?\d+", input())])
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
clen = len(t)
if clen == 0:
    print([i for i in range(n)])
else:
    inverse_adj = [set() for _ in range(n)]
    for second, first in t:
        inverse_adj[second].add(first)
    visited = [0 for _ in range(n)]
    ans = []
    flag = True
    for i in range(n):
        if __dfs(i, inverse_adj, visited, ans):
            print([])
            flag = False
            break
    if flag:
        print(ans)