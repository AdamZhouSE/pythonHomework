import re;

def getInput():
    input_str = input();
    input_str = input_str.replace("\"", '')
    matrixA = [];
    while(input_str != ']'):
        split_list = re.split(',|\[|\]| ', input_str);
        nums = [];
        for i in range(len(split_list)):
            if len(split_list[i]) != 0:
                nums.append(split_list[i]);
        matrixA.append(str(nums));
        input_str = input();
        input_str = input_str.replace("\"", '')

    matrixA = matrixA[1:len(matrixA)]

    matrix = []
    for i in matrixA:
        k = eval(i)
        matrix.append(k)

    return matrix;

def maximalRectangle(matrix):
    maxarea = 0

    dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '0': continue

            # compute the maximum width and update dp with it
            width = dp[i][j] = dp[i][j - 1] + 1 if j else 1

            # compute the maximum area rectangle with a lower right corner at [i, j]
            for k in range(i, -1, -1):
                width = min(width, dp[k][j])
                maxarea = max(maxarea, width * (i - k + 1))
    return maxarea

matrix = getInput()
print(maximalRectangle(matrix))