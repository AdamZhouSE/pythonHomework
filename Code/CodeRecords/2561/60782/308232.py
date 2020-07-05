"""
计算矩阵对的总和
题目描述

给定两个元素大小为N x N的矩阵mat1和mat2。给定值x。问题是要计算两个矩阵之和等于x的所有对。

输入描述

第一行包含一个整数T，即测试用例的数量。每个测试用例的第一行包含两个整数N，x表示平方矩阵的大小。接下来的2 * N行包含N个由空格分隔的整数。

输出描述

对于每个测试用例，打印计数。


"""
times = int(input())
while times > 0:
    times -= 1
    line1 = list(map(int, input().split(" ")))
    n = line1[0]
    x = line1[1]
    matrix1 = []
    matrix2 = []
    answer = 0
    for i in range(n):
        line = list(map(int, input().split(" ")))
        # print(i)
        matrix1 += line
    for j in range(n):
        linew = list(map(int, input().split(" ")))
        # print(j)
        matrix2 += linew
    # print(matrix1)
    # print(matrix2)
    for k in range(len(matrix1)):
        for l in range(len(matrix2)):
            if matrix1[k] + matrix2[l] == x:
                answer += 1
                # print(matrix1[k], matrix2[l])
    print(answer)