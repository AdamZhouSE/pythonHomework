# 题目描述
# 学校有 n 个小组外出游玩，第 i 个小组有 si (1 ≤ si ≤ 4) 个人，
# 同学们想要打出租，每辆车最多坐4个人，同个小组必须坐在同一辆车上，求最少需要多少辆车才能让同学们都坐上出租车
#
# 输入描述
# 第一行为小组数 n (1 ≤ n ≤ 1e5)
# 第二行为 n 个数表示每个小组的人数 si (1 ≤ si ≤ 4)，
# 输出描述
# 输出一个整数表示至少需要的出租车数

n = int(input())
t1 = 0
t2 = 0
t3 = 0
cars = 0
x = input().strip().split(" ")
for i in x:
    if int(i) == 4: cars += 1
    if int(i) == 3: t3 += 1
    if int(i) == 2: t2 += 1
    if int(i) == 1: t1 += 1
# print(cars, t3, t2, t1)
li = range(t3)
for i in li:
    if t1 > 0:
        t1 -= 1
    t3 -= 1
    cars += 1
li = range(t2)
cars += t2 // 2
t2 -= (t2 // 2)*2

if t2 == 0:
    if t1 % 4 == 0:
        cars += t1 // 4
    else:
        cars += t1 // 4 + 1
    t1 = 0
else:
    if t1 >= 2:
        t1 -= 2
        t2 -= 1
        cars += 1
    elif t1 == 1:
        t1 -= 1
        t2 -= 1
        cars += 1
    else:
        t2 -= 1
        cars += 1
    if t1 % 4 == 0:
        cars += t1 // 4
    else:
        cars += t1 // 4 + 1
    t1 = 0
print(cars)