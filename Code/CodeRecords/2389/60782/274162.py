"""
题目描述
    给定一个无重复整数且没有重复的排序数组arr []。
    将数组排序为类似波浪的数组，然后将其返回。
    换句话说，将元素排列为a1> = a2 <= a3> = a4 <= a5 .....的顺序（按照字典顺序递增）。
"""
"""
输入描述
    第一行包含一个整数T，表示测试用例的总数。
    随后是T个测试用例。
    每个测试用例的第一行包含一个整数N，它描述了数组的大小。
    第二行包含数组的N个空格分隔的元素。
"""
"""
输出描述
    对于每个测试用例，在新行中，将数组打印为波形数组。
"""
import math
times = int(input())
while times > 0:
    times = times - 1
    n = int(input())
    the_array = sorted(1, (list(map(int, input().split(" ")))))
    try:   
        for i in range(math.floor(len(the_array) / 2) + 1):
            t = the_array[2 * i]
            the_array[2 * i] = the_array[2 * i - 1]
            the_array[2 * i - 1] = t
    except BaseException:
         for i in the_array:
             print(i, end=" ")
         print()