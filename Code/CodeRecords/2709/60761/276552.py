def stable(bricks,visited):
    ans=0
    for i in range(len(bricks[0])):
        if(bricks[0][i]==1):
            visited[0][i]=1
            joinset(bricks,visited,0,i)
        else:
            visited[0][i]=10
    for i in visited:
        for j in i:
            if(j==1):
                ans+=1
    return ans

def joinset(bricks,visited,x,y):
    if(y==0 and x!=len(bricks)-1):
        if(visited[x+1][y]==0):
            if(bricks[x+1][y]==1):
                visited[x+1][y]=1
                joinset(bricks,visited,x+1,y)
            else:
                visited[x+1][y]=10
        if(visited[x][y+1]==0):
            if(bricks[x][y+1]==1):
                visited[x][y+1]=1
                joinset(bricks,visited,x,y+1)
            else:
                visited[x][y+1]=10
    elif(y==0 and x==len(bricks)-1):
        if(visited[x][y+1]==0):
            if(bricks[x][y+1]==1):
                visited[x][y+1]=1
                joinset(bricks,visited,x,y+1)
            else:
                visited[x][y+1]=10
    elif(y==len(bricks[0])-1 and x!=len(bricks)-1):
        if(visited[x+1][y]==0):
            if(bricks[x+1][y]==1):
                visited[x+1][y]=1
                joinset(bricks,visited,x+1,y)
            else:
                visited[x+1][y]=10
        if(visited[x][y-1]==0):
            if(bricks[x][y-1]==1):
                visited[x][y-1]=1
                joinset(bricks,visited,x,y-1)
            else:
                visited[x][y-1]=10
    elif(y==len(bricks[0])-1 and x==len(bricks)-1):
        if(visited[x][y-1]==0):
            if(bricks[x][y-1]==1):
                visited[x][y-1]=1
                joinset(bricks,visited,x,y-1)
            else:
                visited[x][y-1]=10
    elif(x!=len(bricks)-1):
        if(visited[x+1][y]==0):
            if(bricks[x+1][y]==1):
                visited[x+1][y]=1
                joinset(bricks,visited,x+1,y)
            else:
                visited[x+1][y]=10
        if(visited[x][y-1]==0):
            if(bricks[x][y-1]==1):
                visited[x][y-1]=1
                joinset(bricks,visited,x,y-1)
            else:
                visited[x][y-1]=10
        if(visited[x][y+1]==0):
            if(bricks[x][y+1]==1):
                visited[x][y+1]=1
                joinset(bricks,visited,x,y+1)
            else:
                visited[x][y+1]=10
    else:
        if(visited[x][y-1]==0):
            if(bricks[x][y-1]==1):
                visited[x][y-1]=1
                joinset(bricks,visited,x,y-1)
            else:
                visited[x][y-1]=10
        if(visited[x][y+1]==0):
            if(bricks[x][y+1]==1):
                visited[x][y+1]=1
                joinset(bricks,visited,x,y+1)
            else:
                visited[x][y+1]=10
        
bricks=eval(input())
hits=eval(input())
ans=[]
for i in hits:
    if(bricks[i[0]][i[1]]==1):
        visited=[[0 for i in range(len(bricks[0]))] for j in range(len(bricks))]
        x=stable(bricks[:],visited)
        bricks[i[0]][i[1]]=0
        visited=[[0 for i in range(len(bricks[0]))] for j in range(len(bricks))]
        y=stable(bricks[:],visited)
        ans.append(x-y-1)
    else:
        ans.append(0)
print(ans)