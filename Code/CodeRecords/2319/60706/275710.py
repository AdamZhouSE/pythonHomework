N=int(input())
grid=[]
for i in range(N):
    list1=input().split(',')
    num=[]
    for j in range(len(list1)):
        num.append(int(list1[j]))
    grid.append(num)
ans = 0
for r in range(N):
    for c in range(N):
        if grid[r][c]:
            ans += 2
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r,c+1)):
                if 0 <= nr < N and 0 <= nc < N:
                    nval = grid[nr][nc]
                else:
                    nval = 0

                ans += max(grid[r][c] - nval, 0)
print(ans)