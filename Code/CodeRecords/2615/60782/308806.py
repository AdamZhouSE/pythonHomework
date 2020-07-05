"""
题目描述

给定的是一个长度为L的字符串。任务是从给定的字符串中找到最长的字符串，该字符串的字符按其ASCII码的降序排列并以算术级数排列。希望常见的差异应尽可能小（至少1），并且字符串的字符应具有较高的ASCII值。

输入描述

输入的第一行包含一个整数T，表示测试用例的数量。每个测试包含一个长度为L的字符串。

输出描述

对于每个测试用例，打印最长的字符串。


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
    subs = cut(s)
    # print(subs)
    cur_best = []
    cur_largest = 0
    for ea in subs:
        e = list(ea)
        # print(e)
        if len(e) >1:
            # print(e)
            gap = ord(e[1]) - ord(e[0])
            isValid = True
            for j in range(len(e) - 1):
                if ord(e[j + 1]) - ord(e[j]) != gap:
                    isValid = False
            if len(cur_best) < len(e) and isValid:
                cur_best = e
                # print(e)
                cur_largest = sorted(e)[0]
            elif len(cur_best) == len(e) and cur_largest < sorted(e)[0] and isValid:
                cur_best = e
                # print(e)
                cur_largest = sorted(e)[0]
    # print(cur_best)
    print(''.join(reversed(cur_best)))
