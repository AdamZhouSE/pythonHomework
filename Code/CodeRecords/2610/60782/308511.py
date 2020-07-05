"""
题目描述

给定一个数组。编写一个程序来计算具有所有不同元素的连续子数组的长度总和。

输入描述

输入的第一行包含一个整数T，它表示测试用例的数量。然后是T测试用例。每个测试用例的第一行包含一个整数N，该整数N表示数组中元素的数量。每个测试用例的第二行包含N个以空格分隔的整数。

输出描述

对于每个测试用例，打印具有所有不同元素的连续子数组的长度总和。


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
    n = int(input())
    r = cut(input().split(" "))
    answer = 0
    for i in r:
        if sorted(i) == sorted(list(set(i))):
            answer += len(i)
    print(answer)