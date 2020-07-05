map=eval(input())
n=len(map)
re=[]

def cal(i,j,visited,t):
    visited[i][j]=True
    if i<n-1 and not visited[i+1][j]:
        cal(i+1,j,visited,max(t,map[i][j]))
    if i>0 and not visited[i-1][j]:
        cal(i-1,j,visited,max(t,map[i][j]))
    if j<n-1 and not visited[i][j+1]:
        cal(i,j+1,visited,max(t,map[i][j]))
    if j>0 and not visited[i][j-1]:
        cal(i,j-1,visited,max(t,map[i][j]))
    if i==n-1 and j==n-1:
        re.append(max(t,map[i][j]))

visited=[]
for i in range(0,n):
    temp=[]
    for j in range(0,n):
        temp.append(False)
    visited.append(temp)
cal(0,0,visited,map[0][0])
print(min(re))