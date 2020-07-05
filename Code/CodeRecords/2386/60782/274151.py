"""
题目描述
    给定一个由N个整数组成的数组A，请在数组中找到四个元素的组合，其总和等于给定值X.
"""
"""
输入描述
    第一行包含T个测试用例。
    每个测试用例的第一行都由整数N组成，表示数组中元素的数量。
    第二行由N个间隔的数组元素组成。每个测试用例X的第三行。
"""
"""
输出描述
    单行输出，如果找到组合则输出1，否则输出0。
"""
times = int(input())
while times > 0:
    times = times - 1
    n = int(input())
    the_array = list(map(int, input().split(" ")))
    x = int(input())
    found = 0
    for i in range(len(the_array)):
        for j in range(len(the_array)):
            for k in range(len(the_array)):
                for l in range(len(the_array)):
                    if i != j and i != k and i != l and j != k and j != l and k != l:
                        if the_array[i] + the_array[k] + the_array[j] + the_array[l] == x:
                            found = 1
                            break
    if found == 0:
        print(0)
    elif found == 1:
        print(1)