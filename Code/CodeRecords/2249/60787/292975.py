n=int(input())
grid=[]
for i in range(0,n):
    temp=list(eval(input()))
    grid.append(temp)
a,b,c=0,0,0
for i in range(0,n):
    b+=max(grid[i])
    for j in range(0,n):
        if not grid[i][j]==0:
            a+=1
v=[[i for i in range(0,n)] for j in range(0,n)]
for i in range(0,n):
    for j in range(0,n):
        v[j][i]=grid[i][j]
for i in range(0,n):
    c+=max(v[i])
print(a+b+c)