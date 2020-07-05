def longth(matrix):
    a = len(matrix)
    dics = {}
    nums_max = 1
    if a != 0:
        b = len(matrix[0])
        for i in range(a):
            for j in range(b):
                dics[(i,j)] = matrix[i][j]
        dic_key = dics.keys()
        values = [[1 for i in range(b)] for j in range(a)]
        dics = sorted(dics.items(), key = lambda x: x[1])
        for dic in dics:
            i = dic[0][0]
            j = dic[0][1]
            if (i+1,j) in dic_key and matrix[i+1][j]<matrix[i][j] and values[i][j]<values[i+1][j]+1:
                values[i][j] = values[i+1][j] + 1
            if (i,j+1) in dic_key and matrix[i][j+1]<matrix[i][j] and values[i][j]<values[i][j+1]+1:
                values[i][j] = values[i][j+1] +1
            if (i-1,j) in dic_key and matrix[i-1][j]<matrix[i][j] and values[i][j]<values[i-1][j]+1:
                values[i][j] = values[i-1][j] +1
            if (i,j-1) in dic_key and matrix[i][j-1]<matrix[i][j] and values[i][j]<values[i][j-1]+1:
                values[i][j] = values[i][j-1] + 1
            nums_max = max(nums_max,values[i][j])
    else:
        nums_max = 0

    return nums_max


if __name__ == '__main__':
    a = input()
    b = list(map(int, input()[3:-2].split(",")))
    c = list(map(int, input()[3:-2].split(",")))
    d = list(map(int, input()[3:-1].split(",")))
    f = input()
    # 获得输入的矩阵
    matrix = [b, c, d]
    print(longth(matrix))
