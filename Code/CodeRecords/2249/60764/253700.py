n=int(input())
grid=[]
for i in range(n):
    grid.append(list(map(int,input().split(','))))
s1,s2,s3=0,0,0
for i in range(n):
    for j in range(n):
        if grid[i][j]!=0:
            s1+=1
for i in range(n):
    s2+=max(grid[i])
for j in range(n):
    c=[]
    for i in range(n):
        c.append(grid[i][j])
    s3+=max(c)
print(s1+s2+s3)