inp = input().split(" ")
n, r, avg = int(inp[0]), int(inp[1]), int(inp[2])
data = []
# 需要的总分
require_score = n*avg
# 获取当前总分
curr_score = 0
for i in range(n):
    inp = input().split(" ")
    a, b = int(inp[0]), int(inp[1])
    data.append([b, a])
    curr_score += a
dif = require_score-curr_score
# 如果当前总分大于等于需要的总分，则不需要写论文
if dif <= 0:
    print(0)
else:
    data.sort()
    count = 0
    for i in range(n):
        # 计算所需论文数最小的科目加到满分需要多少篇论文
        dif -= r-data[i][1]
        count += data[i][0] * (r - data[i][1])
        # 如果正好补全差值，则直接退出循环
        if dif == 0:
            break
        # 如果差值为负，则说明写多了
        elif dif < 0:
            count -= (0-dif)*data[i][0]
            break
        # 如果差值为正，则继续循环
    print(count)
