"""
题目描述
    谷歌的招聘团队旨在寻找3名出色的候选人。
    每个候选人的能力都用整数表示。
    如果他们的能力乘积最大，则3名候选人总的来说是令人满意的。
    给定N个候选人的能力，从给定的候选人池中找到最大的集体能力。
"""
"""
输入描述
    输入的第一行包含一个整数T，表示测试用例的数量。
    然后是T测试用例。
    每个测试用例的第一行包含一个整数N，表示候选数。
    每个测试用例的第二行包含N个空格分隔的元素，表示候选者的能力。
"""
"""
输出描述
    对应每个测试用例，在换行符中打印所需的输出（三个候选者的最大集体能力）。
"""
times = int(input())
while times > 0:
    times = times - 1
    n = int(input())
    the_array = list(map(int, input().split(" ")))
    answer = the_array[0] * the_array[1] * the_array[2]
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if the_array[i] * the_array[j] * the_array[k] > answer:
                    answer = the_array[i] * the_array[j] * the_array[k]
    print(answer)