"""
计算差异为k的不重复对
题目描述

给定一个整数数组和一个非负整数k，对所有不同的对进行计数，它们的差等于k，即A [i]-A [j] = k。

输入描述

输入的第一行包括测试用例的数量。 T测试用例的描述如下： 每个测试用例的第一行包含数组的大小，第二行包含数组的元素，第三行包含差k。

输出描述

在每行打印中，数组元素之间存在差k的次数。
"""

times = int(input())
while times > 0:
    times -= 1
    n = int(input())
    array = list(map(int, input().split(" ")))
    k = int(input())
    answer = 0
    fucked = []
    for i in range(len(array)):
        for j in range(len(array)):
            if i < j and abs(array[i] - array[j]) == k and [max(array[i], array[j]), min(array[i], array[j])] not in fucked:
                # print(array[i])
                # print(array[j])
                answer += 1
                fucked.append([max(array[i], array[j]), min(array[i], array[j])])
    print(answer)