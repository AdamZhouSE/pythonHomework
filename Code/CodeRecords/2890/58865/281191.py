pyin = input().split(' ')
n = int(pyin[0])  # 恐怖分子数量
x0 = int(pyin[1])
y0 = int(pyin[2])  # 意大利炮的位置

# 恐怖分子的坐标
arr = []
for i in range(n):
    arr.append([int(i) for i in input().split(' ')])

# 计算所有斜率
k = []
for i in range(n):
    if x0-arr[i][0]==0:
        k.append('ifinity')
    else:
        k.append((y0-arr[i][1])/(x0-arr[i][0]))



print(len(set(k)))
