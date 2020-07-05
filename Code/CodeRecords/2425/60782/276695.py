"""
题目描述
    给定一个排序的整数数组。任务是在数组中找到最接近给定数字的值。
    数组可能包含重复值。
    注意：如果两个值的差相同，则打印大于给定数字的值。
"""
"""
输入描述
    输入的第一行包含一个整数T，表示测试用例的数量。
    然后是T测试用例。
    每个测试用例由两行组成。
    每个测试用例的第一行包含两个整数N和K，第二行包含N个以空格分隔的数组元素。
"""
"""
输出描述
    对于每个测试用例，在新行中打印最接近的数字。
"""
import math
times = int(input())
while times > 0:
    times = times - 1
    line1 = list(map(int, input().split(" ")))
    n = line1[0]
    k = line1[1]
    the_array = list(map(int, input().split(" ")))
    new_array = []
    for i in the_array:
        new_array = new_array + [i - k]
    gap = new_array[0]
    for j in range(n):
        if abs(new_array[j] <= abs(gap)):
            gap = new_array[j]
    print(gap + k)