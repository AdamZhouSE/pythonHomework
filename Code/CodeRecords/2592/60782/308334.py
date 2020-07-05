"""
题目描述

给定一个半径为R的圆形薄片，找出可以从该薄片上切下具有整数长度和宽度的矩形的总数。

输入描述

输入的第一行包含一个整数T，表示测试用例的数量。然后是T测试用例。每个测试用例均包含一个整数R，该整数R表示圆形的半径。

输出描述

对应于每个测试用例，输出一个整数。


"""
import math

times = int(input())
while times > 0:
    times -= 1
    r = int(input())
    answer = 0
    for width in range(1, 2*r):
        for length in range(1, 2*r):
            if width**2 + length**2 <= (2*r)**2:
                answer += 1
    print(answer)