mat = eval(input())
r, c = len(mat), len(mat[0])
for _ in range(r - 1):
    for i in range(r - 1):
        for j in range(c - 1):
            if mat[i][j] > mat[i + 1][j + 1]:
                mat[i][j], mat[i + 1][j + 1] = mat[i + 1][j + 1], mat[i][j]
print(mat)
#s = Solution
#print(s.diagonalSort(mat))