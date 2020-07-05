def isValid(x,y):
    return 0<=x<len(matrix) and 0<=y<len(matrix[0])

def dfs(x,y):
    for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
        nx, ny = x+dx, y+dy
        if isValid(nx,ny) and matrix[nx][ny] == 0:
            matrix[nx][ny] = 1
            dfs(nx,ny)


import re
lst = []
for line in iter(input,']'):
    if line != '[':
        lst.extend(re.findall(r'"(.*?)"',line))
        lst[-1] = lst[-1].replace('\\\\','\\')
n = len(lst)
matrix = [[0 for _ in range(3*n)] for _ in range(3*n)]
for i in range(n):
    for j in range(n):
        if lst[i][j] == '/':
            for k in range(3):
                matrix[3*i+k][3*(j+1)-1-k] = 1
        elif lst[i][j] == '\\':
            for k in range(3):
                matrix[3*i+k][3*j+k] = 1

cnt = 0
for i in range(3*n):
    for j in range(3*n):
        if matrix[i][j] == 0:
            cnt+=1
            matrix[i][j] = 1
            dfs(i,j)
print(cnt)