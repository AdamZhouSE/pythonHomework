word1 = input()
word2 = input()
m = len(word1)
n = len(word2)
line = [0 for i in range(0, n+1)]
matrix = [line.copy() for i in range(0, m+1)]

for i in range(0, m+1):
    matrix[i][0] = i
for i in range(0, n+1):
    matrix[0][i] = i
for i in range(1, m+1):
    for j in range(1, n+1):
        if word1[i-1] == word2[j-1]:
            matrix[i][j] = matrix[i-1][j-1]
        else:
            matrix[i][j] = 1 + min(matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j])
print(matrix[m][n])
