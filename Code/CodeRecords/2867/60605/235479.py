# 题目描述
# 你现在拿到一个由 24 个 0 和 1 个 1 组成的 5*5 的矩阵。
# 现在你需要把这个 1 移动到矩阵的中心点，使得这个矩阵变得 “优雅”，只能上下左右一格一格移动，请你输出最小移动数。
#
# 输入描述
# 描述一个5x5的矩阵，保证输入由 24 个 0 以及 1 个 1 组成
# 输出描述
# 输出最小的移动次数使得矩阵“优雅”

row = -1
col = -1
isDet = False
for i in range(5):
    line = input().strip().split(" ")
    for j in range(5):
        if line[j] == "1":
            row = i
            col = j
            isDet = True
            break
    if isDet:
        break
# print(row, col)
print(abs(row-2)+abs(col-2))

