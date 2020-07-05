# 01矩阵
def getInput():
    matrix = []

    for i in range(3):
        input_str = input()
        line = []
        line.append(int(input_str[0]))
        line.append(int(input_str[2]))
        line.append(int(input_str[4]))
        matrix.append(line)

    return matrix


def getNewMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            l, t = 10001, 10001
            if matrix[i][j] != 0:
                if i > 0:
                    t = matrix[i - 1][j]
                if j > 0:
                    l = matrix[i][j - 1]
                matrix[i][j] = min(l, t) + 1

    for i in range(len(matrix) - 1, -1, -1):
        for j in range(len(matrix[0]) - 1, -1, -1):
            r, b = 10001, 10001
            if matrix[i][j] != 0:
                if i < len(matrix) - 1:
                    b = matrix[i + 1][j]

                if j < len(matrix[0]) - 1:
                    r = matrix[i][j + 1]

                matrix[i][j] = min(matrix[i][j], min(r, b) + 1)
    return matrix

def standardPrint(matrix):
    for i in range(3):
        str_output = str(matrix[i][0])
        for j in range (1, len(matrix[0])):
            str_output += " " + str(matrix[i][j])
        print(str_output)

matrix = getInput()
standardPrint(getNewMatrix(matrix))
