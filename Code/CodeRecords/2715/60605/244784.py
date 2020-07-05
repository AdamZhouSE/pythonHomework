# 题目描述
# 在二维平面上，我们将石头放置在一些整数坐标点上。每个坐标点上最多只能有一块石头。
#
# 现在，move 操作将会移除与网格上的某一块石头共享一列或一行的一块石头。
#
# 我们最多能执行多少次 move 操作？

def find(li, begin):
    while li[begin] != -1:
        begin = li[begin]
    return begin

def union(li, s1, s2):
    li[s1] = s2

stones = list(eval(input()))
ufset = [-1 for i in range(len(stones))]
for i in range(len(stones)):
    for j in range(0, i):
        if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
            union(ufset, find(ufset, i), find(ufset, j))
res = 0
for i in stones:
    if i[1] == -1: res += 1
print(len(stones)-res-1)
