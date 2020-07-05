"""
题目描述

给定数字N。任务是生成并打印具有从1到N的十进制值的所有二进制数。

输入描述

输入的第一行包含一个整数T，它表示测试用例的数量。每个包含N的测试用例只有一行。1 ≤ T ≤ 10^6;1 ≤ N ≤ 10^6

输出描述

在一行中打印所有具有十进制值从1到N的二进制数字。
"""


def d2b(n):
    re = []
    n, m = divmod(n, 2)
    re.append(str(m))
    while n != 0:
        n, m = divmod(n, 2)
        re.insert(0, str(m))
    return ''.join(re) 


times = int(input())
while times > 0:
    times -= 1
    n = int(input())
    for i in range(1,n):
        print(d2b(i), end=" ")
    print(d2b(n), end=" ")
    print()