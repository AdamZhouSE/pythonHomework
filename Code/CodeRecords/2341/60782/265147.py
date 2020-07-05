"""
题目描述
    给定两个排序的数组arr1 []和arr2 []，它们的大小为n和m，并且不递减。
    任务是将两个排序后的数组合并为一个排序后的数组（以非降序排列）。
    注意：预期的时间复杂度为O（（n + m）log（n + m））。请勿使用多余的空间。
    我们需要如下修改现有的数组。
        Input: arr1[] = {10};
               arr2[] = {2, 3};
        Output: arr1[] = {2}
                arr2[] = {3, 10}
        Input: arr1[] = {1, 5, 9, 10, 15, 20};
               arr2[] = {2, 3, 8, 13};
        Output: arr1[] = {1, 2, 3, 5, 8, 9}
                arr2[] = {10, 13, 15, 20}
"""
"""
输入描述
    第一行包含一个整数T，表示测试用例的数量。
    每个测试用例的第一行包含两个以空格分隔的整数X和Y，表示两个排序数组的大小。
    每个测试用例的第二行包含X个空格分隔的整数，表示第一个排序数组P.
    每个测试用例的第三行包含Y个空格分隔的整数，表示第二个数组Q.
"""
"""
输出描述
    对于每个测试用例，请打印（X + Y）以空格分隔的表示合并数组的整数。
"""
times = int(input())
while times > 0:
    times = times - 1
    sizes = list(map(int, input().split(" ")))
    the_array_p = sorted(list(map(int, input().split(" "))))
    the_array_q = sorted(list(map(int, input().split(" "))))
    answer = []
    while len(the_array_p) != 0 and len(the_array_q) != 0:
        if the_array_p[0] > the_array_q[0]:
            answer = answer + [the_array_q[0]]
            del the_array_q[0]
        else:
            answer = answer + [the_array_p[0]]
            del the_array_p[0]
    if len(the_array_p) != 0:
        answer = answer + the_array_p
    else:
        answer = answer + the_array_q
    for i in answer:
        print(i, end=" ")
    print()