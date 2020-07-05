"""
题目描述

给定一个二进制字符串和一个整数K，任务是计算包含k个1的子字符串的数量。

输入描述

输入的第一行包含一个整数T，表示测试用例的数量。然后是T测试用例。每个测试用例包含一个二进制字符串和一个整数K。

输出描述

对于每个测试用例，在新行中打印子字符串的计数。
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
    line = input().split(" ")
    s = line[0]
    k = int(line[1])
    r = cut(s)
    answer = 0
    for i in r:
        counter = 0
        for j in range(len(i)):
            if i[j] == '1':
                counter += 1
        if counter == k:
            answer += 1
    print(answer)
