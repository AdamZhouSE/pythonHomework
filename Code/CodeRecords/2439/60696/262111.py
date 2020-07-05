"""
树上前缀和，边权
"""


class Node:
    def __init__(self):
        self.to = 0     # 目标点
        self.weight = 0     # 边权
        self.father = 0     # 上一个通向它的结点


# 全局变量
visited = []    # 当前结点是否访问过
xor_sum = []    # 当前结点到根节点的和
a = [Node()]  # Node的所有出现情况
h = []  # 记录每个结点在a中最后出现的位置


def dfs(x):
    visited[x] = True
    i = h[x]
    while i != 0:   # 当前结点存在上一次出现
        if not visited[a[i].to]:
            xor_sum[a[i].to] = xor_sum[x] ^ a[i].weight
            dfs(a[i].to)
        i = a[i].father
    return


if __name__ == '__main__':
    n = int(input())
    visited = [False for i in range(n+1)]
    xor_sum = [0 for i in range(n+1)]
    a = [Node() for i in range(2*n-1)]
    h = [0 for i in range(n+1)]
    token = 0
    for i in range(n-1):
        arr = [int(j) for j in input().split()]
        u = arr[0]
        v = arr[1]
        weight = arr[2]
        # 创建一个记录
        token += 1
        a[token].to = v
        a[token].weight = weight
        a[token].father = h[u]
        h[u] = token
        # 创建下一个记录
        token += 1
        a[token].to = u
        a[token].weight = weight
        a[token].father = h[v]
        h[v] = token
    dfs(n)
    m = int(input())
    for i in range(m):
        arr = [int(j) for j in input().split()]
        u = arr[0]
        v = arr[1]
        print(xor_sum[u]^xor_sum[v])