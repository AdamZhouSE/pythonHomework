"""
题目描述

卢卡斯数是一个由以下重复表示的数

Ln = Ln-1 + Ln-2，n> 1

L0 = 2

L1 = 1

现在给定一个数字n，您的任务是找到第n个lucas数字。

注意：由于输出可能很长，因此请使用mod 1000000007

输入描述

输入的第一行包含一个整数T，表示测试用例的数量。然后是T测试用例。每行包含一个整数n。

输出描述

对于每个测试用例，在新行中打印第n个lucas数。


"""


def find(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    answer = 0
    l_1 = find(n - 1)
    l_2 = find(n - 2)
    l_n = l_1 + l_2
    answer += l_n
    # print(answer)
    answer %= 1000000007
    return answer


times = int(input())
while times > 0:
    times -= 1
    n = int(input())
    print(find(n))
