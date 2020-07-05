"""
题目描述
    给定一个由不同整数组成的数组。任务是对所有三元组进行计数，以使两个元素的总和等于第三个元素。
"""
"""
输入描述
    输入的第一行包含一个整数T，表示测试用例的数量。
    然后是T测试用例，每个测试用例由两行组成。
    每个测试用例的第一行包含一个整数N，表示数组的大小，第二行包含N个以空格分隔的元素。
"""
"""
输出描述
    对于每个测试用例，在新行中打印所有三胞胎的计数。
    如果无法形成这样的三元组，请打印“ -1”。
"""
times = int(input())
while times > 0:
    times = times - 1
    n = int(input())
    the_array = list(map(int, input().split(" ")))
    answer = 0
    for i in range(len(the_array)):
        for j in range(len(the_array)):
            for k in range(len(the_array)):
                if i != j and j != k and 1 != k:
                    if the_array[i] + the_array[j] == the_array[k]:
                        answer = answer + 1
    if answer == 0:
        print(-1)
    else:
        print(answer)