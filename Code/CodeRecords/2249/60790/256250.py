n=int(input())
grid=[]
for i in range(0,n):
    line=input().split(",")
    line=list(map(int,line))
    grid.append(line)
ans=0
for i in range(0,n):
    best_row=0
    best_line=0
    for j in range(0,n):
        if(grid[i][j]):ans+=1
        best_row=max(best_row,grid[i][j])
        best_line=max(best_line,grid[j][i])
    ans+=best_row+best_line
print(ans)