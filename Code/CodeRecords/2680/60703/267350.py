T = int(input())
for i in range(T):
    inputList = [int(x) for x in input().split()]
    A,B = inputList[0],inputList[1]
    grid = [[0 for x in range(B)] for y in range(A)]
    # print(grid)
    for j in range(A):
        grid[j][0] = 1
    for j in range(B):
        grid[0][j] =1
    for m in range(1,A):
        for n in range(1,B):
            grid[m][n] = grid[m][n-1] + grid[m-1][n]
    print(grid[A-1][B-1])