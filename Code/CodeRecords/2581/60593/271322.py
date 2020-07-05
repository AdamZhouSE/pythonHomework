n=int(input())
ghost=[]
for i in range(n):
    x,y=map(int,input().split(','))
    ghost.append(x,y)
x,y=map(int,input().split(','))
tar=(x,y)
ans=True
for i in range(n):
    if(abs(tar[0])+abs(tar[1])>=abs(ghost[i][0]-tar[0])+abs(ghost[i][1]-tar[1])):
        ans=False
print(ans)