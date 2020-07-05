"""
题目描述
    给定大小为M * N的矩阵mat [] []。遍历并以螺旋形式打印矩阵。
"""
"""
输入描述
    输入的第一行包含一个整数T，表示测试用例的数量。然后是T测试用例。
    每个测试用例都有2行。第一行包含分别用空格分隔的M和N。第二行包含M * N个值，以空格分隔。
"""
"""
输出描述
    元素以顺时针方向进行螺旋，并以单行显示。
"""


def print_current_edge_1(the_current_matrix):
    for i in the_current_matrix[0]:
        print(i, end=" ")
    the_current_matrix.pop(0)
    # return the_current_matrix


def print_current_edge_2(the_current_matrix):
    for j in range(len(the_current_matrix)):
        print(the_current_matrix[j][-1], end=" ")
        the_current_matrix[j].pop(-1)
    # return the_current_matrix


def print_current_edge_3(the_current_matrix):
    for k in range(len(the_current_matrix[-1])):
        print(the_current_matrix[-1][len(the_current_matrix[-1]) - 1 - k], end=" ")
    the_current_matrix.pop(-1)
    # return the_current_matrix


def print_current_edge_4(the_current_matrix):
    for l in range(len(the_current_matrix)):
        print(the_current_matrix[len(the_current_matrix) - 1 - l][0], end=" ")
        the_current_matrix[len(the_current_matrix) - 1 - l].pop(0)
    # return the_current_matrix


times = int(input())
while times > 0:
    times = times - 1
    line1 = input()
    line2 = input().split(" ")
    m = int(line1.split(" ")[0])
    n = int(line1.split(" ")[1])
    mat = [[] for i in range(m)]
    for i in range(m * n):
        mat[int(i / n)].append(int(line2[i]))
    # print(mat)
    while True:
        try:
            print_current_edge_1(mat)
            print_current_edge_2(mat)
            print_current_edge_3(mat)
            print_current_edge_4(mat)
        except BaseException:
            break
    print()
