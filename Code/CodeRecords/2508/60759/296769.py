def add_edge(f, t, v):
    global cnt
    cnt += 1
    edge.append([head[f], t, v])
    head[f] = cnt   # 以f为起点的第一条边


def tdp(root, num):      # 根节点为root，保留num个节点(计数包括本节点在内，注意不对父节点进行操作)
    if num == 0:
        dp[root][num] = 0
    elif edge[head[root]][0] == 0:         # 叶子节点
        dp[root][num] = value[root]        # num >= 1，dp[root][num]都只能达到value[root]
    else:
        children = []
        is_r = False
        arc = head[root]
        for c in range(2):                # 分别找到左子节点和右子节点
            if is_r:
                arc = edge[arc][0]
            else:
                is_r = True
            if edge[arc][1] == father[root]:
                # 如果拿到的是父节点，找下一条边，避免走到父节点，因为有子节点，所以一定能找到两个子节点
                arc = edge[arc][0]
            child = edge[arc][1]             # 把第一条边的终点作为左子节点
            children.append(child)
            father[child] = root
            value[child] = edge[arc][2]
        for i in range(num):
            if dp[children[0]][i] == 0:
                tdp(children[0], i)
            if dp[children[1]][num - 1 - i] == 0:
                tdp(children[1], num - 1 - i)
            dp[root][num] = max(dp[root][num], value[root] + dp[children[0]][i] + dp[children[1]][num - 1 - i])


# edge = [[next, adj, value], ...]: 下一条边、终点、值
ns, qs = map(int, input().split(' '))
edge = [[0, 0, 0]]
head, value, father = [0 for i in range(ns + 1)], [0 for j in range(ns + 1)], [0 for k in range(ns + 1)]
cnt = 0
for n in range(ns - 1):            # ns个节点，则会输入ns - 1条边
    x, y, val = map(int, input().split(' '))
    add_edge(x, y, val)
    add_edge(y, x, val)
dp = [[0 for q in range(qs + 2)] for root in range(ns + 1)]
# 保留q条边，即保留q + 1个节点
tdp(1, qs + 1)
print(dp[1][qs + 1])
