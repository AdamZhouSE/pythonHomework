'''给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积'''


import ast


def max_s(data):
    row = len(data)
    col = len(data[0])
    max_height = [0 for i in range(col)]
    max_right = [col - 1 for i in range(col)]
    max_left = [0 for i in range(col)]
    max_sum = 0

    for i in range(0,row):
        left = 0
        right = col - 1
        for j in range(0,col):
            if data[i][j] == '1':
                max_height[j] = max_height[j] + 1
                max_left[j] = max(max_left[j],left)
            else:
                max_height[j] = 0
                left = j + 1
                max_left[j] = 0

        j = col - 1
        while j >= 0:
            if data[i][j] == '1':
                max_right[j] = min(max_right[j],right)
            else:
                right = j - 1
                max_right[j] = col - 1
            j -= 1

        for j in range(0,col):
            if (max_right[j] - max_left[j] + 1) * max_height[j] >max_sum:
                max_sum = (max_right[j] - max_left[j] + 1) * max_height[j]

    print(max_sum)

    return


line1 = input()
line2 = input()
matrix = []
while line2 != ']':
    index = line2.index('[')
    if line2.endswith(','):
        line2 = line2[index:len(line2) - 1]
    else:
        line2 = line2[index:]
    matrix.append(ast.literal_eval(line2))
    line2 = input()
max_s(matrix)
