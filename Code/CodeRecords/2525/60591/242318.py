def a(x):
    return x[0]

start = list(map(int,input()[1:-1].split(",")))
end= list(map(int,input()[1:-1].split(",")))
profit = list(map(int,input()[1:-1].split(",")))

dict = {}
for x in range(len(start)):
    dict[(start[x],end[x])] = profit[x]

time = list(dict.keys())
time.sort(key=a)
n = len(start)
# 按结束时间排序
h = sorted(zip(end, start, end, profit))

# 利用动态规划，01背包问题
w = [0] * n
for i in range(n - 1, -1, -1):
    flag = 0
    for j in range(i - 1, -1, -1):
        if h[j][2] <= h[i][1]:
            flag = 1
            w[i] = j
            break
    if flag == 0:
        w[i] = -1
# 计算OPT数组
OPT = [0] * (n + 1)
for i in range(n):
    OPT[i + 1] = max(OPT[i], h[i][3] + OPT[w[i] + 1])
print(OPT[n])
