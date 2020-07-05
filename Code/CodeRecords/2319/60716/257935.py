num = int(input())
grid = list()
for i in range(num):
    strs = input().split(',')
    temp = [int(i) for i in strs]
    grid.append(temp)
bucks = 0
sum = 0
for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j]==0:
            continue
        else:
            bucks+=grid[i][j]
            if grid[i][j]>=2: sum+=(grid[i][j]-1)
            if j==len(grid)-1:continue
            sum+=min(grid[i][j],grid[i][j+1])
            sum+=min(grid[j][i],grid[j+1][i])
print(bucks*6-sum*2)