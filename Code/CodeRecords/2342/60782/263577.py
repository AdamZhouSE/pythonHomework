"""
题目描述
    给定大小为N的正整数数组arr []。反转K个组元素的每个子数组。
"""
"""
输入描述
    输入的第一行包含一个整数T，表示测试用例的数量。然后是T测试用例。
    每个测试用例由两行输入组成。
    每个测试用例的第一行包含一个整数N（数组大小）和一个整数K，中间用空格隔开。
    每个测试用例的第二行包含N个以空格分隔的整数，表示数组元素。
"""
"""
输出描述
    对于每个测试用例，请打印修改后的数组
"""

import math

times = int(input())
while times > 0:
    times = times - 1
    line1 = list(map(int, input().split(" ")))
    line2 = list(map(int, input().split(" ")))
    num = math.ceil(line1[0] / line1[1])
    answer = [[] for i in range(num)]
    for i in range(line1[0]):
        answer[int(i / line1[1])].append(line2[i])
    for j in answer:
        j.reverse()
    answer = sum(answer, [])
    for i in answer:
        print(i, end=" ")