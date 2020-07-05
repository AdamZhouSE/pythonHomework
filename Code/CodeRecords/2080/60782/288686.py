"""
题目描述
    按照给定的起始顶点广度优先遍历图，每一次通过字母顺序选择顶点查找下一层邻接点，打印遍历顺序。
"""
"""
输入描述
    输入第一行为测试用例个数，后面每一个用例用多行表示。
    用例第一行是节点个数n和开始顶点，用空格隔开。
    后面n+1行为图的邻接矩阵，其中第一行为节点名称。
    值之间使用空格隔开。
"""
"""
输出描述
    输出遍历顺序，用空格隔开。
"""


def find_next(nodey):
    index = find_index.get(nodey)
    ind_ans = -1
    for l in range(n):
        if matrix[index][l] == '1':
            ind_ans = l
            break
    curr_node = find_node.get(ind_ans)
    print(" " + curr_node, end="")
    for m in range(n):
        matrix[m][ind_ans] = '0'

    over_yet = True
    for j in range(n):
        for k in range(n):
            if matrix[j][k] == '1':
                over_yet = False
                break
    if not over_yet:
        find_next(curr_node)
    else:
        return
    return


times = int(input())
while times > 0:
    times = times - 1
    line1 = input()
    n = int(line1.split(" ")[0])
    start = line1.split(" ")[1]
    nodes = list(map(str, input().split(" ")))

    matrix = []
    for i in range(n):
        temp_input = list(input().split(" "))
        del temp_input[0]
        matrix.append(temp_input)
    find_index = {}
    find_node = {}
    for i in range(n):
        find_node.update({i: nodes[i]})
        find_index.update({nodes[i]: i})
    # print(matrix)
    # print(dic)
    print(start, end="")
    for o in range(n):
        matrix[o][0] = '0'
    find_next(start)
    print()
