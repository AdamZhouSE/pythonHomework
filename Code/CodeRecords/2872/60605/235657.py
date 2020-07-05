# 题目描述
# 桌子上有 n 个石头排成一排，可能为红色，绿色和蓝色，请你移除最少数量的石头使得相邻石头的颜色均不同。
#
# 输入描述
# 输入第一行为石头的个数 n (1 ≤ n ≤ 50)
# 第二行为一个字符串 s，表示每个石头的颜色，用 R, G 或 B 表示
# 输出描述
# 输出一个数，表示最少需要移除的石头数

n = int(input())
li = list(input().strip())
newli = []
lastColor = "N"
for i in li:
    if lastColor != i:
        lastColor = i
        newli.append(i)
print(len(li)-len(newli))