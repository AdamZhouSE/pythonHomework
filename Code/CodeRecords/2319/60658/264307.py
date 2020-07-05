n = int(input())
li = []
for i in range(n):
    li.append([int(x) for x in input().split(",")])
ans = 0
for i in range(n):
    for j in range(n):
        if li[i][j]>0:
            ans+=2
            for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                nv=0
                if 0<=x<n and 0<=y<n:
                    nv = li[x][y]
                ans+=max(li[i][j]-nv,0)
print(ans)