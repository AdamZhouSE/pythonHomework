"""
题目描述
    给定一个大小为N的整数数组。
    假定“ 0”为无效数字，所有其他均为有效数字。
    编写程序以如下方式修改数组：
        如果下一个数字是有效数字并且与当前数字相同，则将当前数字值加倍，并将下一个数字替换为0。
        修改后，重新排列数组，使所有0都为移至末尾，则有效数字或新的双倍数字的顺序将保持原始数组中的顺序。
"""
"""
输入描述
    输入的第一行包含一个整数T，表示测试用例的数量。
    然后是T测试用例。
    每个测试的第一行包含一个整数N，它表示数组的大小。
    然后，下一行包含N个以空格分隔的整数，它们表示数组的元素。
"""
"""
输出描述
    For each test case print space separated elements of the new modified array on a new line.
"""
times = int(input())
while times > 0:
    times = times - 1
    n = int(input())
    the_array = list(map(int, input().split(" ")))
    try:
        for i in range(len(the_array)):
            if the_array[i + 1] != 0 and the_array[i + 1] == the_array[i]:
                the_array[i] = 2 * the_array[i]
                the_array[i + 1] = 0
    except BaseException:
        answer = []
        for j in the_array:
            if 0 != j:
                answer = answer + [j]
        for k in range(len(the_array) - len(answer)):
            answer = answer + [0]
        for l in range(len(answer) - 1):
            print(answer[l], end=" ")
        print(answer[-1])
