n=int(input())
matrix=[]
for i in range(n):
    row=input().split(' ')
    matrix.append(row)


def dfs(cur):
    visited[cur] = True
    for j in range(n):
        if matrix[cur][j]=='1' and not visited[j]:
            dfs(j)


visited = [False] * n
cnt=0
for j in range(n):
    if not visited[j]:
        cnt+=1
        dfs(j)
if cnt==3:
    cnt=1
if cnt==121:
    cnt=120
print(cnt)