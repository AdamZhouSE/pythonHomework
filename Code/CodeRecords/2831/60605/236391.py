# 题目描述
# 某地铁环线有 n 个车站。 我们知道所有邻近站点之间的距离：
#
# d[1] 是第 1 站和第 2 站之间的距离;
# d[2] 是第 2 站和第 3 站之间的距离;
# ......
# d[n-1] 是第 n-1 和第 n 个站之间的距离;
# d[n]是第 n 个站和第 1 个站之间的距离。
# 列车沿着两个方向的环线。 找到站点 s 和 t 之间的最短距离。
#
# 输入描述
# 第一行包含整数 n（3≤n≤100)，表示环线上的站数
# 第二行包含 n 个整数（1≤d[i]≤100） 表示相邻站对之间的距离。
# 第三行包含两个整数 s 和 t（1≤s,t≤n） 表示站点 s 和 t
# 输出描述
# 输出站点 s 和 t 之间的最短距离

n = int(input())
tmp = input().strip().split(" ")
ttmp = input().strip().split(" ")
li = []
for i in tmp: li.append(int(i))
s = int(ttmp[0])-1
t = int(ttmp[1])-1
s1 = min(s, t)
s2 = max(s, t)

round1 = 0
for i in range(s1, s2):
    round1 += li[i]
round2 = 0
for i in range(s2, len(li)):
    round2 += li[i]
for i in range(0, s1):
    round2 += li[i]
print(min(round2, round1))