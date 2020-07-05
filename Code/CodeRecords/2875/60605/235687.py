# 题目描述
# 小佩蒂娅在家里组织了一个新年聚会，邀请了 n 个朋友来，朋友间要互相交换礼物。
# 她藏起了她的礼物，并观察朋友们相互送礼物，她记住了谁给谁礼物，且每个人都只获得了一个礼物。
#
# 现在小佩蒂娅想知道每个朋友的礼物分别是谁送的，请你帮助她。
#
# 输入描述
# 第一行为一个整数 n 表示朋友的数量
# 第二行为 n 个整数，第 i 个数表示第 i 个朋友送给了朋友 ai 一个礼物
# 输出描述
# 输出 n 个数，分别表示这 n 个朋友分别收到了谁的礼物

n = int(input())
li = []
a = input().strip().split()
for i in range(n):
    li.append([i+1, int(a[i])])
li = sorted(li, key=lambda l: l[1])
for i in range(n):
    print(li[i][0], end="")
    if i != n-1: print(" ", end="")
print()