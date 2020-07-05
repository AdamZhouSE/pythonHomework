temp=input()[2:-2].split("],[")
ans=[]
for i in temp:
    ans.append([int(x) for x in i.split(",")])
n = len(ans)
depth = -1
visited = set()
que = [(i, j) for i in range(n) for j in range(n) if ans[i][j]]
if not que or len(que) == n * n:
    print(-1)
else:
    while que:
        depth += 1
        nodes, que = que[:], []
        for node in nodes:
            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x, y = node[0] + i, node[1] + j
                if 0 <= x < n and 0 <= y < n and not ans[x][y] and (x, y) not in visited:
                    visited.add((x, y))
                    que.append((x, y))
    print(depth)