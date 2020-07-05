"""
题目描述
    给定一个N大小的数组。d小于等于N，以d个元素为一组将数组进行旋转。
        Example :
            Input :  arr[] = [1, 2, 3, 4, 5, 6, 7]
                     d = 2
        Output : arr[] = [3, 4, 5, 6, 7, 1, 2]
    每两个元素为一组，即1和2为一组，3和4为一组，以此类推。第一组转到最后，第二组转为第一组。
"""
"""
输入描述
    输入的第一行包含一个整数T，表示测试用例的数量。然后是T测试用例。每个测试用例包含三行。
    每个测试用例的第一行由整数N组成，其中N是数组的大小。 
    每个测试用例的第二行包含N个以空格分隔的整数，表示数组元素。
    每个测试用例的第三行包含“ d”。
"""
"""
输出描述
    对应于每个测试用例，在新行中打印修改后的数组。
"""

import math

times = int(input())
while times > 0:
    n = int(input())
    line2 = input()
    d = int(input())
    the_array = line2.split(" ")
    for chars in the_array:
        chars = int(chars)
    num = math.ceil(n / d)
    the_whole_picture = [[] for i in range(num)]
    for i in range(n):
        the_whole_picture[int(i / d)].append(int(the_array[i]))
    the_whole_picture.append(the_whole_picture[0])
    the_whole_picture.pop(0)
    the_whole_picture = sum(the_whole_picture, [])
    for j in the_whole_picture:
        print(j, end=" ")
    print()