#08
# 思考分成xyz分别观察，求出线上的面积
# 最终解法：立方体个数*6 - 接触面*2
# 这题目真正输入和样例不一样,要处理
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
            sum += grid[i][j] #计算立方体的个数
        if grid[i][j] > 1:
            num += (grid[i][j]-1) #Z轴方向的接触面
        if i+1<n and grid[i+1][j] != 0:
            num += min(grid[i][j],grid[i+1][j]) #后面的接触面
        if j+1<n and grid[i][j+1] != 0:
            num += min(grid[i][j],grid[i][j+1]) #右边的接触面

number = sum*6 - num*2
print(number)