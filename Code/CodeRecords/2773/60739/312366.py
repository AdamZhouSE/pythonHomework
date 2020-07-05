import re;

def getInput():
    input_str = input();
    input_str = input();

    matrixA = [];
    while(input_str != ']'):
        split_list = re.split(',|\[|\]| ', input_str);
        nums = [];
        for i in range(len(split_list)):
            if len(split_list[i]) != 0:
                nums.append(int(split_list[i]));
        matrixA.append(nums);
        input_str = input();

    return matrixA;

def getLength(matrix_a, matrix_b, matrix_c, i, j):
    current_num = matrix_b[i + 1][j + 1];
    a = matrix_b[i][j + 1];
    b = matrix_b[i + 1][j + 2];
    c = matrix_b[i + 2][j + 1];
    d = matrix_b[i + 1][j];

    if a <= current_num and b <= current_num and c <= current_num and d <= current_num:
        matrix_c[i + 1][j + 1] = 1;
        return;

    else:
        return;

def getMaxLength(matrix_a):
    m = len(matrix_a);
    n = len(matrix_a[0]);

    matrix_b = [[-10] * (m + 2) for i in range(n + 2)];
    for i in range (m):
        for j in range (n):
            matrix_b[i + 1][j + 1] = matrix_a[i][j];
    # print(matrix_b);
    return 0;

def longestIncreasingPath(matrix) -> int:
    if matrix is None or matrix == []:
        return 0
    dp = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
    res = 1
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            res = max(res, process(matrix, i, j, dp))
    return res

def process(matrix, i, j, dp):
    '''
    以i，j开头的最长递增路径
    '''
    if dp[i][j] != 0:
        return dp[i][j]
    res = 1
    p1, p2, p3, p4 = 1, 1, 1, 1
    if i - 1 >= 0 and matrix[i][j] < matrix[i - 1][j]:
        p1 += process(matrix, i - 1, j, dp)
    if j - 1 >= 0 and matrix[i][j] < matrix[i][j - 1]:
        p2 += process(matrix, i, j - 1, dp)
    if i + 1 < len(matrix) and matrix[i][j] < matrix[i + 1][j]:
        p3 += process(matrix, i + 1, j, dp)
    if j + 1 < len(matrix[0]) and matrix[i][j] < matrix[i][j + 1]:
        p4 += process(matrix, i, j + 1, dp)
    dp[i][j] = max(res, p1, p2, p3, p4)
    return dp[i][j]



if __name__ == '__main__':
    nums = getInput();
    
    print(longestIncreasingPath(nums));
