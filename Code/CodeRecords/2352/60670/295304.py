def inrange(x,y):
    global x1,y1,x2,y2
    if x>=x1 and x<=x2 and y>=y1 and y<=y2:
        return True
    else:
        return False

def search(x,y):
    global square,visited
    visited[x][y]=True
    if inrange(x+1,y) and square[x+1][y]==1 and (not visited[x+1][y]):
        search(x+1,y)
    elif inrange(x-1,y) and square[x-1][y]==1 and (not visited[x-1][y]):
        search(x-1,y)
    elif inrange(x,y+1) and square[x][y+1]==1 and (not visited[x][y+1]):
        search(x,y+1)
    elif inrange(x,y-1) and square[x][y-1]==1 and (not visited[x][y-1]):
        search(x,y-1)
    return

n,m,q=map(int,input().split())
square=[]
for i in range(0,n):
    line=list(input())
    for j in range(0,len(line)):
        line[j]=int(line[j])
    square.append(line)
for t in range(0,q):
    visited=[[False for i in range(0,m)]for i in range(0,n)]
    x1,y1,x2,y2=map(int,input().split())
    x1-=1
    y1-=1
    x2-=1
    y2-=1
    num=0
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if square[i][j]==1 and (not visited[i][j]):
                search(i,j)
                num+=1
    print(num)