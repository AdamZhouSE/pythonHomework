from typing import List
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        for k in range(1, min(m,n)):
            for i in range(m-k):
                for j in range(n-k):
                    if mat[i][j] > mat[i+1][j+1]:
                        mat[i][j], mat[i+1][j+1] = mat[i+1][j+1], mat[i][j]
        return mat


if __name__=="__main__":
    s=eval(input())
    x=Solution().diagonalSort(s)
    print(x)