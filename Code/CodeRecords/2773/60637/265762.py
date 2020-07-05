line=input()
matrix=[]
while(True):
    line=input().strip()
    if(line==']'):
        break
    if(line[len(line)-1]==','):
        line=line[:-1]
    matrix.append(eval(line))
m=len(matrix)
n=len(matrix[0])
memory = [[0] * n for i in range(m)]
def dfs(i,j):
    global matrix,memory,m,n
    if(not memory[i][j]):
        ans = 0
        num = matrix[i][j]
        if i > 0 and matrix[i - 1][j] > num:
            ans = max(ans, dfs(i - 1, j))
        if j > 0 and matrix[i][j - 1] > num:
            ans = max(ans, dfs(i, j - 1))
        if i < m - 1 and matrix[i + 1][j] > num:
            ans = max(ans, dfs(i + 1, j))
        if j < n - 1 and matrix[i][j + 1] > num:
            ans = max(ans, dfs(i, j + 1))
        memory[i][j] = ans + 1
    return memory[i][j]
ans = 0
for i in range(m):
    for j in range(n):
        ans = max(ans, dfs(i, j))
print(ans)

