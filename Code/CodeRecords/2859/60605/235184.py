# 题目描述
# 瓦莱拉是一个小男孩。
# 昨天他在学校里完成了一项艰巨的数学任务，因此瓦莱拉没有足够的时间正确学习英语字母表。
# 不幸的是，英语老师决定今天对字母进行测试。
# 在测试中，瓦莱拉得到了一张 n*n 的方格纸，每个单位正方形包含英语字母的一些小写字母。
#
# 瓦莱拉需要知道方形纸上书写的字母是否为字母“ X”。 瓦莱拉的老师认为，在下列情况下，纸上的字母形成“ X”：
#
# 在方格纸的两个对角线上，所有字母均相同；
#
# 纸张的所有其他正方形（它们不在对角线上）包含与对角线上的字母不同，但都是同一个字母。
#
# 帮助瓦莱拉，为他编写完成上述任务的程序。
#
# 输入描述
# 第一行为方格纸的边长 n (3 ≤ n < 300; n 是奇数)
# 接下来 n 行，每行为长度为 n 的字符串，用来表示方格纸上的字母
# 输出描述
# 如果形成 X，输出 YES，否则输出 NO

n = int(input())
li = []
for i in range(n):
    x = list(input().strip())
    for j in x:
        li.append(j)

dig = li[0]
oth = None
isX = True
for i in range(n):
    for j in range(n):
        idx = i*n+j
        if i == j or j == n-1-i:
            if li[idx] != dig:
                isX = False
                break
        else:
            if oth is None:
                oth = li[idx]
            else:
                if oth != li[idx]:
                    isX = False
                    break
    if not isX: break
if n == 1: print("NO")
else:
    if isX: print("YES")
    else: print("NO")
