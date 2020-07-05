map=eval(input())
n=len(map)
re=[]

def cannotMove(i,j,visited):
    if i<0 or i>n-1 or j<0 or j>n-1:
        return True
    if visited[i][j]:
        return True
    return False

def cal(i,j,visited,t):
    if cannotMove(i+1,j,visited) and cannotMove(i-1,j,visited) and cannotMove(i,j+1,visited) and cannotMove(i,j-1,visited) and not(i==n-1 and j==n-1):
        return
    if i==n-1 and j==n-1:
        re.append(t)
    else:
        if j<n-1 and not visited[i][j+1]:
            visited[i][j+1]=True
            cal(i,j+1,visited,max(t,map[i][j+1]))
            visited[i][j+1]=False
        if j>0 and not visited[i][j-1]:
            visited[i][j-1]=True
            cal(i,j-1,visited,max(t,map[i][j-1]))
            visited[i][j-1]=False
        if i<n-1 and not visited[i+1][j]:
            visited[i + 1][j]=True
            cal(i+1,j,visited,max(t,map[i+1][j]))
            visited[i + 1][j]=False
        if i>0 and not visited[i-1][j]:
            visited[i - 1][j]=True
            cal(i-1,j,visited,max(t,map[i-1][j]))
            visited[i - 1][j]=False

visited=[]
for i in range(0,n):
    temp=[]
    for j in range(0,n):
        temp.append(False)
    visited.append(temp)
visited[0][0]=True
cal(0,0,visited,map[0][0])
print(min(re))