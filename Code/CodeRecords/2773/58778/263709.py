matrix=[]
for i in range(10000):
    s=input()
    if(s!='[' and s!=']'):
        if(s[len(s)-1:len(s)]==','):
            matrix.append(eval(s[2:len(s)-1]))
        else:
            matrix.append(eval(s[2:]))

    if(s==']'):
        break
def longestIncreasingPath(matrix):
    if not matrix or not matrix[0]:return 0

    row=len(matrix)
    col=len(matrix[0])
    lookup=[[0]*col for _ in range(row)]#可以快速建立一个全0矩阵

    def dfs(i,j):
        if lookup[i][j]!=0:
            return lookup[i][j]
        res=1
        for x,y in [[-1,0],[1,0],[0,1],[0,-1]]:#x,y分别是列表的两项
            tmp_i=x+i
            tmp_j=y+j
            if 0<=tmp_i<row and 0<=tmp_j<col and matrix[tmp_i][tmp_j]>matrix[i][j]:
                res=max(res,1+dfs(tmp_i,tmp_j))#继续搜索，res表示以当前位置结尾的递增长度
        lookup[i][j]=max(res,lookup[i][j])
        return lookup[i][j]

    return max(dfs(i,j)for i in range(row) for j in range(col))
print(longestIncreasingPath(matrix))