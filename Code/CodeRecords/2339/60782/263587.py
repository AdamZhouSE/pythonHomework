"""
题目描述
    给定正整数数组。任务是找到数组的反转计数。 反转计数：对于数组，反转计数指示数组要排序的距离（或距离）。
    如果数组已经排序，则反转计数为0。如果数组以相反顺序排序，则反转计数为最大。
    形式上，如果a [i]> a [j]且i <j，则两个元素a [i]和a [j]形成一个反转。
"""
"""
输入描述
    输入的第一行包含一个整数T，表示测试用例的数量。每个测试用例的第一行是N，即数组的大小。每个测试用例的第二行包含N个元素。
"""
"""
输出描述
    打印数组的反转计数。
"""
times = int(input())
while times > 0:
    n = int(input())
    line2 = input()
    the_array = line2.split(" ")
    counter = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if int(the_array[i]) > int(the_array[j]):
                counter = counter + 1
    print(counter)