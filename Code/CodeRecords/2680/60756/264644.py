T=int(input())
for t in range(T):
    x=input().split()
    A=int(x[0])
    B=int(x[1])
    grid=[[0 for i in range(B)] for j in range(A)]
    grid[0][0]=1
    for i in range(A):
        for j in range(B):
            if i!=A-1:
                grid[i+1][j]+=grid[i][j]
            if j!=B-1:
                grid[i][j+1]+=grid[i][j]
    print(grid[-1][-1])