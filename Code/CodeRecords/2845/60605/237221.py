# 题目描述
# 一天，Dima 和 Alex 就笔记本电脑的价格和质量发生了争执。
# 迪玛认为笔记本电脑越贵越好，Alex 不同意。 Alex 认为存在价格更低，但质量更好（价格严格小于且质量严格大于）的笔记本。
#
# 我们为您介绍了 n 台笔记本电脑。请问这些笔记本电脑中是否存在支持 Alex 观点的一台。
#
# 输入描述
# 第一行为笔记本电脑的台数 n (1 ≤ n ≤ 10^5)
# 接下来 n 行每行为每台笔记本的价格 ai 和质量 bi (1 ≤ ai, bi ≤ n)，bi 越大说明质量越好。
# 保证 ai 均不同，bi 也均不同
# 输出描述
# 若 Alex 的观点是对的，输出 Happy Alex，否则输出 Poor Alex

n = int(input())
li = []
for i in range(n):
    x = input().strip().split()
    li.append([int(x[0]), int(x[1])])

isExist = False
li = sorted(li, key=lambda v : v[0])
for i in range(0, n):
    for j in range(i-1, -1, -1):
        if li[j][1] > li[i][1] and li[j][0] != li[i][0]:
            isExist = True
            break
    if isExist: break

if isExist: print("Happy Alex")
else: print("Poor Alex")

