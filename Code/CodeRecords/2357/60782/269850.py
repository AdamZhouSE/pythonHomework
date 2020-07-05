"""
题目描述
    给定两个大小不同的元素的未排序数组A和B，A的大小为N，B的大小为M，任务是从两个数组中求和等于X的所有对。
"""
"""
输入描述
    输入的第一行包含一个整数T，表示测试用例的数量。
    然后是T测试用例。每个测试用例包含3行。
    第一行包含3个以空格分隔的整数N，M，X。
    然后在接下来的两行中分别为数组A和B的以空格分隔的值。
"""
"""
输出描述
    对于新行中的每个测试用例，请打印所有对u，v对的排序后的空格分隔值，其中u属于数组A，v属于数组B。
    如果不存在这样的对，则打印-1。
"""
times = int(input())
while times > 0:
    times = times - 1
    line1 = input().split(" ")
    n = int(line1[0])
    m = int(line1[1])
    x = int(line1[2])
    the_array_A = list(map(int, input().split(" ")))
    the_array_B = list(map(int, input().split(" ")))
    for i in the_array_A:
        for j in the_array_B:
            if i + j == x:
                print(i, end=" ")
                print(j)