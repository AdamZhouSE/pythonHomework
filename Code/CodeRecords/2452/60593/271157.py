N=int(input())
grid=[]
for _ in range(N):
    line=list(map(int,input().split(',')))
    grid.append(line)
tar=int(input())
ans=False
for _ in grid:
    if(tar in _):
        ans=True
        break
print(ans)
    