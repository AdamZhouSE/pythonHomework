N=int(input())
grid=[]
for _ in range(N):
    line=list(map(int,input().split(',')))
    grid.append(line)
tar=int(input())
print(tar in grid)
    