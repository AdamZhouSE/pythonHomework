n=int(input())
grid=[]
for i in range(n):
    list1=input().split(',')
    num=[]
    for j in range(len(list1)):
        num.append(int(list1[j]))
    grid.append(num)
N = len(grid)
ans = 0
for i in range(N):
    best_row = 0 
    best_col = 0  
    for j in range(N):
        if grid[i][j]: ans += 1 
        best_row = max(best_row, grid[i][j])
        best_col = max(best_col, grid[j][i])

    ans += best_row + best_col
print(ans)