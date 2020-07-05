"""
题目描述
    给定一个正整数数组，其中所有数字均出现偶数次，但一个数字出现奇数次。查找该数字。
"""
"""
输入描述
    输入的第一行包含一个整数T，表示测试用例的数量。
    然后是T测试用例。
    每个测试用例由两行组成。
    每个测试用例的第一行由整数N组成，其中N是数组的大小。
    每个测试用例的第二行包含N个以空格分隔的整数，表示数组元素。
"""
"""
输出描述
    对应于每个测试用例，打印出现奇数次的数字。
    如果不存在这样的元素，则打印0
"""
times = int(input())
while times > 0:
    times = times - 1
    n = int(input())
    the_array = sorted(list(map(int, input().split(" "))))
    answer = 0
    current = 1
    for i in range(1, n + 1):
        if the_array[i] != the_array[i - 1]:
            if current % 2 == 1:
                answer = the_array[i - 1]
                break
            else:
                current = 1
        else:
            current = current + 1
    print(answer)