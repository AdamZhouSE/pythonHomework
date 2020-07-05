"""
题目描述
    给一个n(1<=n<=2500)个点m(1<=m<=6200)条边的无向图，求s到t的最短路。
"""
"""
输入描述
    第一行四个由空格隔开的整数n、m、s、t。
    之后的m行，每行三个正整数s_i（符号“_”表示下标）、t_i、w_i(1<=W_i<=10^9)，表示一条从s_i到t_i长度为w_i的边。
"""
"""
输出描述
    一个整数表示从s到t的最短路长度。数据保证至少存在一条道路。
"""
# line1 = list(map(int, input().split(" ")))
# n = line1[0]
# m = line1[1]
# s = line1[2]
# t = line1[3]
# the_graph = [[]] * m
# for i in range(m):
#     tmp = list(map(int, input().split(" ")))
#     the_graph[i] = tmp
# # print(the_graph)
# # 节点名字为结果数组里他位置的下标 - 1
# num_of_links = 1
# answer = [-1] * n
# settled = [False] * n
# answer[s - 1] = 0
# settled[s - 1] = True
# cur_shortest = -1
# cur_shortest_end = -1
#
# # 确认每个节点的直接相连的节点都有哪些
# direct_links = [[]] * m
# # direct_lengths = [[]] * m
# for i in range(n):
#     tmp1 = set([])
#     for pair in the_graph:
#         if pair[0] == i + 1:
#             tmp1.update({pair[1]})
#         if pair[1] == i + 1:
#             tmp1.update({pair[0]})
#     direct_links[i] = list(tmp1)
#     direct_lengths[i] = list(tmp2)

# 初始化：直接连接
# for pairs in the_graph:
#     if pairs[0] == s:
#         answer[pairs[1] - 1] = pairs[2]
#         settled[pairs[1] - 1] = True
#         if cur_shortest < 0 or cur_shortest > pairs[2]:
#             cur_shortest = pairs[2]
#             cur_shortest_end = pairs[1]
#     if pairs[1] == s:
#         answer[pairs[0] - 1] = pairs[2]
#         answer[pairs[0] - 1] = True
#         if cur_shortest < 0 or cur_shortest > pairs[2]:
#             cur_shortest = pairs[2]
#             cur_shortest_end = pairs[0]

# print(cur_shortest)
# print(answer)
# print(direct_links)
# print(direct_lengths)

# while num_of_links < n:
#     try:
#         num_of_links += 1
#         for nodes in range(len(answer)):
#             if answer[nodes] == -1:

# cost = [[0x3f] * 3000] * 3000
# cost = [0x3f] * 9000000
cost = [[0x3f for i in range(1000)] for i in range(1000)]

vis = [0] * 2505

# print(cost)

line1 = list(map(int, input().split(" ")))
n = line1[0]
m = line1[1]
s = line1[2]
t = line1[3]

for i in range(m):
    tmp = list(map(int, input().split(" ")))
    s0 = tmp[0]
    t0 = tmp[1]
    w0 = tmp[2]
    cost[s0][t0] = min(cost[s0][t0], w0)
    cost[t0][s0] = min(cost[t0][s0], w0)

d = [0x3f] * 2505
d[s] = 0

while True:
    v = -1
    for j in range(1, n + 1):
        if vis[j] == 0 and (v == -1 or d[j] < d[v]):
            v = j;
    if v == -1:
        break;
    vis[v] = 1

    for k in range(1, n + 1):
        d[k] = min(d[k], d[v] + cost[v][k])

print(d[t])
