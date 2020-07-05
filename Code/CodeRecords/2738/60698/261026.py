# 14
left = input()
matrix = []
area = 0
while True:
    line = input()
    if line == ']':
        break
    else:
        if line[-1] == ',':
            line = line[0:len(line) - 1]
        line = eval(line)
        matrix.append(list(map(int, line)))
dp = [[(0, 0)] * len(matrix[0]) for _ in range(0, len(matrix))]
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        if matrix[i][j] == 1:
            try:
                horizontal = dp[i][j - 1][0] + 1
            except:
                horizontal = 1
            try:
                vertical = dp[i - 1][j][1] + 1
            except:
                vertical = 1
            dp[i][j] = (horizontal, vertical)
            length = horizontal
            width = vertical
            for k in range(0, vertical):
                if dp[i - k][j][0] < length:
                    length = dp[i - k][j][0]
            area1 = length * width
            length = horizontal
            width = vertical
            for l in range(0, horizontal):
                if dp[i][j - l][1] < width:
                    width = dp[i][j - l][1]
            area2 = length * width
            if area < max(area1, area2):
                area = max(area1, area2)
print(area)


