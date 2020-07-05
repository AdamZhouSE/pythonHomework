n=int(input())
grid=[]
front,left,bottom=0,0,0
for _ in range(n):
    a=list(map(int,input().split(',')))
    grid.append(a)
    left+=max(a)
    for i in a:
        if i!=0:
            bottom+=1
for i in range(n):
    MAX=0
    for j in range(n):
        MAX=max(MAX,grid[j][i])
    front+=MAX
print(front+left+bottom)    