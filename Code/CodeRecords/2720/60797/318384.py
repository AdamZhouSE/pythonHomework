# tag

from collections import deque
n=int(input())
connections=eval(input())
num_component = 0  #G中连通分量的数目
num_remains = 0    #G中冗余边的数目

# 构建图G的邻接表表示：
G = []
for i in range(0, n):
    G.append([])
for pair in connections:
    G[pair[0]].append(pair[1])
    G[pair[1]].append(pair[0])

# 以BFS统计G中连通分量和冗余边的数目：
color = [0] * n
for computer in range(0, n):
    if (color[computer] != 0):
        continue
    # 对新发现的包含computer的连通分量进行遍历
    num_component += 1
    num_node = 0  # 该连通分量中的结点数
    num_degree = 0  # 该连通分量中所有结点度的和
    Q = deque([])
    Q.append(computer)
    color[computer] = 1
    while (len(Q) != 0):
        u = Q.popleft()
        num_node += 1
        for v in G[u]:
            if not color[v]:
                color[v] = 1
                Q.append(v)
            num_degree += 1
    num_remains += (num_degree / 2) - (num_node - 1)

# 判断是否可行：
if num_component - 1 <= num_remains:
    print(num_component - 1)
else:
    print(-1)