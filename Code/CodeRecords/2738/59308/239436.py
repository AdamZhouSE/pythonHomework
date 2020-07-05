import re
pattern = re.compile('[0-9]+')

matrix = list()
while True:
    a = input()
    if a != "[" and a != "]":
        a = pattern.findall(a)
        matrix.append(a)
    if a == ']':
        break
dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
maxarea = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == '0':
            continue
        width = dp[i][j] = (dp[i][j-1] + 1) if j else 1
        for k in range(i, -1, -1):
            width = min(width, dp[k][j])
            maxarea = max(maxarea, width * (i-k+1))
print(maxarea)



