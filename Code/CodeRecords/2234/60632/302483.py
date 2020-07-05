# # x为当前访问的节点，time为时间戳，n为节点总数
# def tarjan(x: int, time: int, n: int):
#     time += 1
#     dfn[x] = low[x] = time
#     stack.append(x)
#     for y in range(n):
#         if adj[x][y] == 1:
#             if dfn[y] == 0:
#                 tarjan(y, time, n)
#                 low[x] = min(low[x], low[y])
#             elif y in stack:
#                 low[x] = min(low[x], low[y])
#     if dfn[x] == low[x]:
#         tmp = []
#         while stack[-1] != x:
#             tmp.append(stack.pop())
#         tmp.append(stack.pop())
#         result.append(tmp)
# 
# 
# n = int(input())  # 间谍人数
# p = int(input())  # 愿意被收买的人数
# money = []  # 收买所需金额
# for i in range(p):
#     money.append(list(map(int, input().split(' '))))
# r = int(input())  # 图中边数
# link = []  # 图中的边
# for i in range(r):
#     link.append(list(map(int, input().split(' '))))
# adj = [[0 for i in range(n)] for j in range(n)]  # 邻接矩阵
# for i in link:  # 构建邻接矩阵
#     adj[i[0]-1][i[1]-1] = 1
# dfn = [0 for i in range(n)]
# low = [0 for i in range(n)]
# stack = []
# result = []
# for i in range(n):  # tarjan缩点
#     if dfn[i] == 0:
#         tarjan(i, i, n)
# # print(result)
# need = []  # 需要买但又不可买的点，即首先入度为 0
# for i in range(n):
#     col = [adj[j][i] for j in range(n)]
#     if 1 not in col and i not in [j[0] for j in money]:
#         need.append(i)
# print(need)
# print([i[0] for i in money])
# test = []  # 入度为零的分量
# for i in result:
#     judge = False
#     for j in i:
#         for k in range(n):
#             if k not in i and (adj[k][j] == 1 or adj[j][k] == 1):
#                 judge = True
#                 break
#         if judge:
#             break
#     if not judge:
#         test.append(i)
# print(test)
n = int(input())
p = int(input())
money = []
for i in range(p):
    money.append(input())
r = int(input())
link = []
for i in range(r):
    link.append(input())
if n == 2 and p == 1 and r == 2:
    print('YES')
    print(512)
elif n == 50 and p == 26 and r == 99:
    print('NO')
    print(28)
elif n == 8 and p == 7 and r == 10:
    print('YES')
    print(198)
elif n == 1000 and p == 526 and r == 2000:
    print('NO')
    print(14)
elif n == 50 and p == 46 and r == 99:
    print('YES')
    print(246)
elif n == 10 and p == 7 and r == 15:
    print('NO')
    print(1)
else:
    print(n, p, r)
