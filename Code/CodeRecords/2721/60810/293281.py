'''
给定两个表示两个整数值的二进制字符串，请找到两个字符串的乘积。
例如，如果第一位字符串为“ 1100”，第二位字符串为“ 1010”，则输出应为120
'''


def doMulti(s1, s2):
    binS1 = int(s1, 2)
    binS2 = int(s2, 2)
    res = binS1 * binS2
    print(res)


n = int(input())
for i in range(0, n):
    inp = input().split(' ')
    s1 = str(inp[0])
    s2 = str(inp[1])
    doMulti(s1, s2)