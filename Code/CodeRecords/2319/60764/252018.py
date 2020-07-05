n=int(input())
grid=[]
for a in range(n):
    grid.append(list(map(int,input().split(','))))
s1,s2,s3=0,0,0
for i in grid:
    for j in i:
        if j>0:
            s1+=1
for i in grid:
    s2+=max(i)
for i in range(len(grid[0])):
    tem=[]
    for j in range(len(grid)):
        tem.append(grid[j][i])
    s3+=max(tem)
print((s1+s2+s3)*2)