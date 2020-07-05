"""
题目描述

给定一个字符串，您需要打印具有恰好k个唯一字符的最长子字符串的大小。如果没有可能的子字符串，则打印-1。

例

对于字符串abacbebebe和k = 3，子字符串将为cbebebe，长度为7。

输入描述

输入的第一行包含一个整数T，表示测试用例的数量，然后是T个测试用例。每个测试用例包含两行。每个测试用例的第一行包含一个字符串s，下一行包含一个整数k。

输出描述

对于换行中的每个测试用例，请打印所需的输出。
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
    s = input()
    k = int(input())
    r = cut(s)
    k_length = []
    answer = 0
    for i in r:
        if len(set(i)) == k:
            k_length.append(i)
    for l in k_length:
        if len(l) > answer:
            answer = len(l)
    print(answer)