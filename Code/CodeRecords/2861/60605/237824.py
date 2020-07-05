# 题目描述
# 有n个学生想要去参加一个比赛，他们每个人的能力为 ai，每个学生每做一道题就能让自己的能力提升一级。
#
# 已知只有相同能力的人才能组队，一个队伍为两人，请问如果每个人都需要队友，那么所有人总共至少需要做多少道题才能达成条件？
#
# 输入描述
# 第一行输入 n (2 <= n <=100) 保证 n 为偶数
# 第二行输入 n 个数字 (1<=ai<=100), ai 为第 i 个学生的能力值.
# 输出描述
# 输出一个整数表示所有人总共至少要做多少题

n = int(input())
k = input().strip().split(" ")
li = []
for i in k:
    li.append(int(i))
length = len(li)
li = sorted(li)
minl = 0
tot = 0
for i in range(0, length//2):
    minDist = li[len(li) - 1] - li[0]
    for l in range(0, len(li)-1):
        if li[l+1]-li[l] < minDist:
            minDist = li[l+1]-li[l]
            minl = l
    try:
        del li[minl]
        del li[minl]
    except IndexError:
        # print(k)
        pass
    tot += minDist
print(tot)
