dirs = [
    [0,1],[1,0],[0,-1],[-1,0]
]
m = 0
n = 0

def dfs(matrix:list,i:int,j:int,cache:list):
    if(cache[i][j]!=0): return cache[i][j]
    for dir in dirs:
        x = dir[0]+i
        y = dir[1]+j
        if 0<=x and x<m and 0<=y and y< n and matrix[x][y]>matrix[i][j]:
            cache[i][j] = max(cache[i][j],dfs(matrix,x,y,cache))
    cache[i][j]+=1
    return cache[i][j]


def longestIncreasingPath(matrix:list):
    if len(matrix)==0:
        return 0
    m = len(matrix)
    n = len(matrix[0])
    cache = [[0 for x in range(n)] for y in range(m)]
    ans = 0
    for i in range(m):
        for j in range(n):
            ans = max(ans,dfs(matrix,i,j,cache))
    return ans

matrix = eval(input())
print(longestIncreasingPath(matrix))