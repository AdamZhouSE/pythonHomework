class Solution(object):
    def updateMatrix(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                l,t= 10001,10001
                if matrix[i][j] != 0:
                    if i > 0: 
                        t = matrix[i - 1][j]
                    if j > 0:
                        l = matrix[i][j - 1] 
                    matrix[i][j] = min(l,t) + 1

        for i in range(len(matrix) - 1, -1 ,-1):
            for j in range(len(matrix[0]) - 1, -1, -1):
                r,b = 10001,10001
                if matrix[i][j] != 0:
                    if i < len(matrix) - 1: 
                        b = matrix[i + 1][j]  
                    if j < len(matrix[0]) - 1:
                        r = matrix[i][j + 1] 
                    matrix[i][j] = min(matrix[i][j], min(r,b) + 1)
        return matrix
lis=[]
for i in range(0,3):
    lis.append(list(map(int,input().split(' '))))
matrix=lis
ss = Solution()
re = ss.updateMatrix(matrix)
for i in range(0,3):
    for j in range(0,3):
        if j!=2:
            print(re[i][j],end=' ')
        else:
            print(re[i][j])