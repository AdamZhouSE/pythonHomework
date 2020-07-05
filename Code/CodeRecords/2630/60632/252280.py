# 本题即求每条路径中的最高高度中的最小值，即每一步都向周围高度最低的平台移动

data = list(eval(input()))
n = len(data)  # n*n的方格
result = 0
i, j = 0, 0
data[0][0] = '*'
while i != n - 1 or j != n - 1:
    north = data[i - 1][j] if i != 0 and data[i - 1][j] != '*' else n * n
    south = data[i + 1][j] if i != n - 1 and data[i + 1][j] != '*' else n * n
    west = data[i][j - 1] if j != 0 and data[i][j - 1] != '*' else n * n
    east = data[i][j + 1] if j != n - 1 and data[i][j + 1] != '*' else n * n
    nextStep = min(north, south, west, east)
    if nextStep > result:
        result = nextStep
    if nextStep == north:
        i -= 1
    elif nextStep == south:
        i += 1
    elif nextStep == west:
        j -= 1
    elif nextStep == east:
        j += 1
    data[i][j] = '*'
print(result)
