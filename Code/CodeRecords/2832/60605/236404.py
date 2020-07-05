# 题目描述
# 伊万最近买了一本侦探小说。
# 这本书非常有趣，以至于本书的每一页都有一个谜，稍后将对此进行解释。
# 第 i 页包含的一些秘密，将在第 a[i] (a[i]>=i) 页上进行解释.
#
# 伊万想读完整本书。
# 每天，他都会从未阅读过的一页开始，并继续逐页阅读，直到对他所读的所有奥秘都得到解释
# （伊万结束这一天的阅读当且仅当不存在一个下标 i，使得伊万今天读过第 i 页但没有读过第 a[i] 页）。
#
# 请输出伊万读完整本书所需要的天数。
#
# 输入描述
# 第一行包括一个整数n (1<=n<=10^4) 表示这本书的页数。
# 第二行包含 n 个整数 a[1]，a[2]，…，a[n]（i≤a[i]≤n），其中 a[i] 是页数，其中包含第 i 页的奥秘解释。
# 输出描述
# 输出一个整数表示伊万读完整本书所需要的天数

n = int(input())
li = []
t = input().strip().split(" ")
for i in t:
    li.append(int(i)-1)
cnt = 0
resli = []
for i in range(n):
    resli.append(li[i])
    resli = sorted(resli)
    maxPage = resli[len(resli)-1]
    if maxPage <= i:
        resli=[]
        cnt+=1
print(cnt)