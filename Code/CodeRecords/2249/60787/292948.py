n=int(input())
grid=[]
for i in range(0,n):
    temp=list(eval(input()))
    grid.append(temp)
a,b,c=0,0,0
for i in range(0,len(grid)):
    b+=max(grid[i])
    for j in range(0,len(grid[i])):
        if not grid[i][j]==0:
            a+=1
v=[i for i in grid]
for i in range(0,len(grid)):
    for j in range(0,len(grid[i])):
        v[j][i]=grid[i][j]
for i in range(0,len(v)):
    c+=max(v[i])
print(a+b+c)