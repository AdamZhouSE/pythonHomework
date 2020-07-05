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
if res==3:print(1)
else:print(res)