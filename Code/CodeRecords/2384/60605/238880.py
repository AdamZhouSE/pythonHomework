# 题目描述
# 给定一个N个整数的数组arr []。任务是查找数组中缺失的最小正数。 注意：使用不变的额外空间，可以在O（n）时间内获得期望的解。
#
# 输入描述
# 第一行包含T个测试用例。每个测试用例的第一行由N组成，表示数组中的元素数。每个测试用例的第二行由数组中的元素组成。
#
# 输出描述
# 单行输出，打印丢失的最小正数。
#
# 输入范例
# 2
# 5
# 1 2 3 4 5
# 5
# 0 -10 1 3 -20
# 输出范例
# 6
# 2

t = int(input())
liN = []
liNums = []
for i in range(t):
    liN.append(int(input()))
    x = input().strip().split(" ")
    ll = []
    for j in x:
        if int(j) > 0:
            ll.append(int(j))
    liNums.append(ll)

for k in range(t):
    for i in range(1, 10000):
        if i not in liNums[k]:
            print(i)
            break

