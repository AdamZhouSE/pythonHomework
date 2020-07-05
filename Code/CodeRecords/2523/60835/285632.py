class Solution:
    def diagonalSort(self, mat):
        r, c = len(mat), len(mat[0])
        for _ in range(r - 1):
            for i in range(r - 1):
                for j in range(c - 1):
                    if mat[i][j] > mat[i + 1][j + 1]:
                        mat[i][j], mat[i + 1][j + 1] = mat[i + 1][j + 1], mat[i][j]
        return mat
matrix = eval(input())
s = Solution
print(s.diagonalSort(matrix))