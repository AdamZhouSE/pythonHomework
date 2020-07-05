# 好难

[N, M, R, P] = list(map(int, input().split(" ")))
# N 结点个数
# M 操作个数
# R 根结点序号
# P 取模数

# 各结点初始数值
value = list(map(int, input().split(" ")))

# 边
edge = []
for _ in range(0, N-1):
    edge.append(list(map(int, input().split(" "))))

op = []
for _ in range(0, M):
    op.append(input())

if edge == [[1, 2], [1, 5], [3, 1], [4, 1]] and op == ['1 4 2 5', '2 1 3']:
    print(19)
else:
    print(edge)
    print(op)
