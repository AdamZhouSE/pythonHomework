"""
题目描述
    给定两个大小分别为M和N的排序数组A和B以及元素k。我们的任务是找到位于最终排序数组第k个位置的元素。
"""
"""
输入描述
    输入的第一行包含一个整数T，表示测试用例的数量。随后是T个测试用例。
    每个测试用例的第一行由3个整数M，N和K组成，分别表示A中的元素数M，B中的元素数N和第k个位置元素。
    每个测试用例的第二行和第三行分别由A和B元素组成。
"""
"""
输出描述
    将元素打印在第K个位置。
"""
times = int(input())
while times > 0:
    times = times - 1
    line1 = input().split(" ")
    string_a = input()
    string_b = input()
    string_a = list(map(int, string_a.split(" ")))
    string_b = list(map(int, string_b.split(" ")))
    answer = []
    while len(string_a) > 0 and len(string_b) > 0:
        answer = answer + [min(string_a[0], string_b[0])]
        if string_b[0] > string_a[0]:
            del string_a[0]
        else:
            del string_b[0]
    if len(string_a) != 0:
        answer = answer + string_a
    else:
        answer = answer + string_b

    print(answer[int(line1[2]) - 1])