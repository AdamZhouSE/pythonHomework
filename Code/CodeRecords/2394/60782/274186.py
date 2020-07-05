"""
题目描述
    给定一个正整数数组A。将给定数组的所有零推到数组的末尾。
"""
"""
输入描述
    第一行包含一个整数T，表示测试用例的总数。
    在每个测试用例中，第一行是数组N中元素的数量，下一行是数组元素。
"""
"""
输出描述
    最后将全0移后打印数组。
"""
times = int(input())
while times > 0:
    times = times - 1
    n = int(input())
    the_array = list(map(int, input().split(" ")))
    answer = []
    for i in the_array:
        if i != 0:
            answer = answer + [i]
    for j in range(len(the_array) - len(answer)):
        answer = answer + [0]
    for k in range(len(answer)):
        print(answer[k], end=" ")
    print()