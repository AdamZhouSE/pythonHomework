"""
题目描述
    给定大小为N的非负整数的未排序数组A，找到一个连续的子数组，该数组加到给定的数字S上。
"""
"""
输入描述
    输入的第一行包含一个整数T，表示测试用例的数量。
    然后是T测试用例。
    每个测试用例由两行组成。
    每个测试用例的第一行是N和S，其中N是数组的大小，S是总和。
    每个测试用例的第二行包含N个以空格分隔的整数，表示数组元素。
"""
"""
输出描述
    对于每个测试用例，在新行中，如果sum等于子数组，则从左边开始打印第一个出现的子数组的开始和结束位置（1个索引），否则打印-1。
"""
times = int(input())
while times > 0:
    times = times - 1
    n = int(input())
    s = int(input())
    the_array = list(map(int, input().split(" ")))
    start = 0
    end = 0
    for i in range(len(the_array) - 1):
        sum = the_array[i]
        start = i
        for j in range(i + 1, len(the_array)):
            sum = sum + the_array[j]
            if sum == s:
                end = j
                break
        break
    if end > start:
        print(start + 1, end=" ")
        print(end + 1)
    else:
        print(-1)