import bisect
grid=eval(input())
n=len(grid)
seen={(0,0)}
r=[[grid[0][0],0,0]]
num=0
while True:
    h,i,j=r.pop(0)
    num=max(num,h)
    if(i==j==n-1):
        print(num)
        break
    for x,y in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
        if(0<=x<n and 0<=y<n and (x,y) not in seen):
            bisect.insort(r, [grid[x][y], x, y])        
            seen|={(x, y)}
