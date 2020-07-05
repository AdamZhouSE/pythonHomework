# 题目描述
# 有n个同学（编号为1到n）正在玩一个信息传递的游戏。
# 在游戏里每人都有一个固定的信息传递对象，
# 其中，编号为i的同学的信息传递对象是编号为Ti的同学。
# 游戏开始时，每人都只知道自己的生日。
# 之后每一轮中，所有人会同时将自己当前所知的生日信息告诉各自的信息传递对象
# （注意：可能有人可以从若干人那里获取信息，但是每人只会把信息告诉一个人，即自己的信息传递对象）。
# 当有人从别人口中得知自己的生日时，游戏结束。请问该游戏一共可以进行几轮？

n = int(input())
x = input().strip().split(" ")
li = []
for i in x:
    li.append(int(i)-1)
cnt = 0
info = [[j] for j in range(n)]
isKnown = False
while not isKnown:
    cnt+=1
    for i in range(n):
        for j in info[i]:
            info[li[i]].append(j)
    for i in range(n):
        if i in info[i][1:]:
            isKnown = True
            break
print(cnt+1)
