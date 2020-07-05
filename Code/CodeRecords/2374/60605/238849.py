# 题目描述
# 给定整数数组A []，请根据元素的频率对数组进行排序。
# 也就是说，频率较高的元素排在第一位。如果两个元素的频率相同，则以较小的数字为准。
#
# 输入描述
# 输入的第一行包含一个整数T，表示测试用例的数量。
# T测试用例的描述如下。每个测试用例的第一行包含一个表示数组大小的整数N。
# 第二行包含N个以空格分隔的整数A1，A2，...，AN，它们表示数组的元素。
#
# 输出描述
# 对于每个测试用例，在新行中将每个排序的数组打印在单独的行中。对于每个数组，其编号应以空格分隔
import collections
def solve(n, lii):
    # n = int(input())
    # lii = input().strip().split(" ")
    li = []
    for i in lii:
        li.append(int(i))
    c = collections.Counter(li)

    c = sorted(c.items(), key=lambda vi:(vi[0]))
    c = sorted(c, key=lambda vi:(vi[1]), reverse=True)
    res = ""
    for j in c:
        for k in range(j[1]):
            res = res + str(j[0]) + " "
    print(res)


t = int(input())
ooo = []
lll = []
for i in range(t):
    ooo.append(int(input()))
    lll.append(input().strip().split(" "))

for i in range(t):
    solve(ooo[i], lll[i])

# print()