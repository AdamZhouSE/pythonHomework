# 学校运动会即将来临，某年级将表演腰鼓。
# 腰鼓有两面，一面是红色的，一面是白色的。
# 假设一共有N（1<=N<=20,000）个同学表演，表演刚开始每一个鼓都是红色面朝向观众，
# 舞蹈老师会发出M（1<=M<=20,000）个指令，如果指令发给第i个表演的同学,这位同学就会把腰鼓反过来，
# 如果腰鼓之前是红色面朝向观众的,那么就会变成白色面朝向观众，
# 如果腰鼓之前是红色面朝向观众的,那么就会变成白色面朝向观众，
# 反之亦然。那么问题来了（！？），在老师每一次发出指令后，
# 找到最长的连续的一排同学，满足每相邻的两个手中的腰鼓朝向观众的一面互不相同，输出这样一排连续的同学的人数。

x = input().strip().split()
n, m = int(x[0]), int(x[1])
orders = []
for i in range(m):
    orders.append(int(input()))
peoples = [True for i in range(n)]

res = []
for i in orders:
    peoples[i-1] = not peoples[i-1]
    # print(peoples)
    maxContiOne = 0
    tempContiOne = 0
    for i in range(1, n):
        if peoples[i] != peoples[i - 1]:
            tempContiOne += 1
        else:
            if tempContiOne != 0:
                maxContiOne = max(maxContiOne, tempContiOne)
                tempContiOne = 0
    if tempContiOne != 0: maxContiOne = max(maxContiOne, tempContiOne)
    res.append(maxContiOne+1)



for i in res:
    print(i)



