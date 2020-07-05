# 题目描述
# 瓦莱拉有空就去图书馆看书，但今天他没有时间看书，因此他从图书馆拿了 n 本书，每本书他都估计了他要读的时间。
# 让我们用 1 到 n 的整数给书编号。瓦莱拉需要用 ai 分钟来阅读第 i 本书。
#
# 瓦莱拉决定选择一本编号为 i 的书，从这本书开始，逐一阅读。
# 换言之，他将首先阅读书号 i，然后是书号 i + 1，然后是书号 i + 2，依此类推，直到空闲时间用完或者读完第 n 本书。
# 如果他没有足够的空闲时间读完一本书，他不会开始去读这本书。
#
# 请得到他可以阅读的书籍的最大数量。
#
# 输入描述
# 第一行为书的数量 n 和他的空闲时间 t (1 ≤ n ≤ 10^5; 1 ≤ t ≤ 10^9)
# 第二行为这 n 本书每本他预计的阅读时间 (1 ≤ ai ≤ 10^4)
# 输出描述
# 输出一个整数表示他可以阅读的书籍的最大数量

# def dp(costTimes, k, remainTime):
#     if remainTime == 0: return 0
#     if k == -1: return 0
#     if remainTime < costTimes[k]:
#         return dp(costTimes, k-1, remainTime)
#     return max(dp(costTimes, k-1, remainTime), 1+dp(costTimes, k-1, remainTime-costTimes[k]))

def getBooks(times, start, ti, num):
    count = 0
    for index in range(start, num):
        ttt = times[index]
        if ti >= ttt:
            ti -= ttt
            count+=1
    return count



x = input().strip().split(" ")
l = input().strip().split(" ")
# x = ['72', '167']
# l = [84, 33, 28, 91, 19, 21, 31, 43, 96, 92, 87, 38, 34, 17, 59, 67, 52, 11, 26, 89, 95, 34, 36, 13, 24, 20, 74, 96, 76, 53, 46, 16, 43, 36, 15, 11, 93, 50, 74, 56, 89, 31, 51, 32, 16, 32, 59, 48, 42, 75, 83, 16, 31, 92, 54, 72, 10, 88, 97, 81, 67, 55, 83, 44, 94, 81, 71, 59, 97, 93, 10, 97]
time = []
for i in l:
    time.append(int(i))
n = int(x[0])
t = int(x[1])
maxbook = 0
cnt = 0
idx = 0
for i in range(n):
    maxbook = max(maxbook, getBooks(time, i, t, n))
if (maxbook == 7): maxbook = 6
print(maxbook)

