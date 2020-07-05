#08
# 思考分成xyz分别观察，求出线上的面积
# 这题目真正输入和样例不一样，我也是吐了
n = int(input())
grid = []
for i in range(0,n):
    ori = input().split(",")
    part = [int(item) for item in ori]
    grid.append(part)
# print(grid)

sum = 0
num = 0
for i in range(0,n):
    for j in range(0,n):
        if grid[i][j] != 0:
            sum += grid[i][j]
        if grid[i][j] > 1:
            num += (grid[i][j]-1)
        if i+1<n and grid[i+1][j] != 0:
            num += min(grid[i][j],grid[i+1][j])
        if j+1<n and grid[i][j+1] != 0:
            num += min(grid[i][j],grid[i][j+1])

number = sum*6 - num*2
print(number)