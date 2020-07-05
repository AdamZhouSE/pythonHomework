"""
题目描述

给定一个仅包含0、1或2s的字符串，请计算具有相等数量0、1s和2s的子字符串的数量。

例子：

输入：str =“ 0102010”

输出2

说明：

子字符串str [2，4] =“ 102”，并且

子字符串str [4，6] =“ 201”

输入描述

输入的第一行包含一个整数T，表示测试用例的数量。然后是T测试用例。每个测试用例包含一行。该行包含0、1和2的字符串。

输出描述

对应于每个测试用例，在新的一行中，打印计数所有可能的具有相同的0、1、2和2s数目的子字符串。


"""


def cut(s: str):
    results = []
    # x + 1 表示子字符串长度
    for x in range(len(s)):
        # i 表示偏移量
        for i in range(len(s) - x):
            results.append(s[i:i + x + 1])
    return results


times = int(input())
while times > 0:
    times -= 1
    r = cut(input())
    answer = 0
    for i in r:
        num_0 = 0
        num_1 = 0
        num_2 = 0
        for j in range(len(i)):
            if i[j] == '0':
                num_0 += 1
            if i[j] == '1':
                num_1 += 1
            if i[j] == '2':
                num_2 += 1
        if num_1 == num_2 == num_0:
            answer += 1
    print(answer)
