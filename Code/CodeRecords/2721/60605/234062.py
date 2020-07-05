# 题目描述
# 给定两个表示两个整数值的二进制字符串，请找到两个字符串的乘积。例如，如果第一位字符串为“ 1100”，第二位字符串为“ 1010”，则输出应为120
#
# 输入描述
# 第一行包含T个测试用例。每个测试用例中只有一行包含2个二进制字符串。
#
# 输出描述
# 单行输出，打印相乘的值。

t = int(input())
li = []
for i in range(t):
    newli = input().split(" ")
    newnewli = []
    newnewli.append(int(newli[0], base=2))
    newnewli.append(int(newli[1], base=2))
    li.append(newnewli)

for i in range(t):
    print(li[i][0] * li[i][1])