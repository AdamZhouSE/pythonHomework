arrayString=input()
s=eval(arrayString)
n=len(s)
ans=0
for r in range(n):
    for c in range(n):
        if s[r][c]:
            ans+=2
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r,c+1)):
                if 0 <= nr < n and 0 <= nc < n:
                    nval = grid[nr][nc]
                else:
                    nval = 0
                ans += max(grid[r][c] - nval, 0)    
print(ans)                    
            
