def completeMatirx(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]==1:
                matrix[j][i]=1
def bfs(matrix,path,ind):
    while ind<len(path):
        for i in range(len(matrix)):
            if matrix[path[ind]][i]==1 and i not in path:
                path.append(i)
        ind+=1
n=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))
completeMatirx(matrix)
path=[0]
res=1
ind=0
while True:
    bfs(matrix,path,ind)
    if len(path)<n:
        res+=1
        for i in range(n):
            if i not in path:
                path.append(i)
                break
    else:
        break
print(res)