row = int(input())
a = []
for t in range(row):
    a.append([int(i) for i in input().split(',')])
col = len(a[0])
mem = [[0]*col for _ in range(row)]
for i in range(row-1,-1,-1):
    for j in range(col-1,-1,-1):
        if i==row-1 and j==col-1:
            mem[i][j] = max(0,-a[i][j])
        elif i==row-1:
            mem[i][j] = max(0,mem[i][j+1]-a[i][j])
        elif j==col-1:
            mem[i][j] = max(0,mem[i+1][j]-a[i][j])
        else:
            mem[i][j] = max(0,min(mem[i+1][j],mem[i][j+1])-a[i][j])
print(mem[0][0]+1)