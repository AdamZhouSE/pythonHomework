R=int(input())
C=int(input())
grid=[]
r0=int(input())
c0=int(input())
for i in range(R):
    for j in range(C):
        grid.append([i,j])
grid.sort(key=lambda x:abs(x[0]-r0)+abs(x[1]-c0))
print(grid)