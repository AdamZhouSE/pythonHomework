"""
隔离链接列表中的偶数和奇数节点
题目描述

给定整数链接列表，编写一个函数来修改链接列表，以使所有偶数出现在修改后的链接列表中的所有奇数之前。另外，请保持偶数和奇数的顺序相同。

输入描述

输入的第一行包含一个整数T，它表示测试用例的数量。 每个测试用例的第一行是N，N是链表中元素的数量。 每个测试用例的第二行在链表中包含N个输入元素。1 ≤ T ≤ 100;1 ≤ N ≤ 100;1 ≤ size of elements ≤ 1000

输出描述

在修改后的“链表”中打印所有偶数，然后打印奇数。
"""
times = int(input())
while times > 0:
    times -= 1
    n = int(input())
    array = list(map(int, input().split(" ")))
    odd = []
    even = []
    for i in array:
        if i % 2 == 0:
            even.append(i)
        if i % 2 == 1:
            odd.append(i)
    answer = even + odd
    for j in answer:
        print(j, end=" ")
    print()