# 好难

[N, M, R, P] = list(map(int, input().split(" ")))
# N 结点个数
# M 操作个数
# R 根结点序号
# P 取模数

# 各结点初始数值
value = input()

# 边
edge = []
for _ in range(0, N-1):
    edge.append(list(map(int, input().split(" "))))

op = []
for _ in range(0, M):
    op.append(input())

print(edge)
print(op)