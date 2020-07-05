import re


def max_matrix(matrix):
    max_area = 0
    dp = [[0] * len(matrix[0]) for x in range(len(matrix))]
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == '1':
                if j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j-1] + 1
            width = dp[i][j]
            for k in range(i, -1, -1):
                width = min(width, dp[k][j])
                max_area = max(max_area, width*(i-k+1))
    return max_area


mat = []
inp = input()
while True:
    inp = input()
    if inp == ']':
        break
    row = re.split(r"[\[\]\",]", inp)
    while "" in row:
        row.remove("")
    mat.append(row)
print(max_matrix(mat))
