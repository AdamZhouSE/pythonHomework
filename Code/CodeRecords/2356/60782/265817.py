"""
题目描述
    给定大小为N的未排序数组。找到数组中的第一个元素，使其所有左元素都较小，而所有右元素都大于它。
    注意：左侧和右侧元素可以等于所需元素。并且极端元素不能是必需元素。
"""
"""
输入描述
    输入的第一行包含一个整数T，表示测试用例的数量。
    然后是T测试用例。每个测试用例由两行组成。
    每个测试用例的第一行包含一个整数N，表示数组的大小，第二行包含N个以空格分隔的数组元素。
"""
"""
输出描述
    对于每个测试用例，在新行中打印所需的元素。如果数组中没有这样的元素，则打印-1。
"""
times = int(input())
while times > 0:
    times = times - 1
    n = int(input())
    the_array = list(map(int, input().split(" ")))
    answer = -1
    for i in range(1, len(the_array) - 1):
        is_ok = True
        for j in range(i):
            if the_array[j] > the_array[i]:
                is_ok = False
                break
        for k in range(i + 1, len(the_array)):
            if the_array[k] < the_array[i]:
                is_ok = False
                break
        if is_ok:
            answer = the_array[i]
            break
    print(answer)