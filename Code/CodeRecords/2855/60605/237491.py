# 题目描述
# Toastman 提出了一个非常简单的任务。
# 他将其提供给 Appleman，但 Appleman 不知道如何解决。 你能帮他吗？
#
# 给定 n×n 棋盘。 板上的每个单元格都有字符 x 或字符 o。请确认板上的每个单元格上下左右合计都有偶数个的 o（0 也是偶数）。
#
# 输入描述
# 第一行为棋盘的大小 n (1 ≤ n ≤ 100)
# 接下来 n 行，每行为一个长度为 n 的字符串，共同表示这个棋盘
# 输出描述
# 如果每个单元格周围都有偶数个 o，输出 YES，否则输出 NO

n = int(input())
li = ""
for i in range(n):
    li = li + input().strip()
li = list(li)
isFine = True
for i in range(n):
    for j in range(n):
        # i, j 坐标
        cnt = 0
        if 0 <= i-1 < n and li[(i-1) * n + j] == "o":
            cnt += 1
        if 0 <= i+1 < n and li[(i+1) * n + j] == "o":
            cnt += 1
        if 0 <= j-1 < n and li[i * n + j-1] == "o":
            cnt += 1
        if 0 <= j+1 < n and li[i * n + j+1] == "o":
            cnt += 1
        if cnt % 2 == 1:
            # print(i, j)
            isFine = False
            break
        # print(i, j)
    if not isFine: break

if isFine:
    print("YES")
else:
    print("NO")
