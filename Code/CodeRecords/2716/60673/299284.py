def find(parent, x):
    if (parent[x] == x):
        return parent[x]
    return find(parent, parent[x])

def union(parent, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)
    if (x_root != y_root):
        parent[x_root] = y_root

def union_find(grid):
    n=len(grid)
    parent=[i for i in range(4*n*n)]
    for r,row in enumerate(grid):
        for c,val in enumerate(row):
            top=4*(r*n+c)
            if val in ['/',' ']:
                union(parent,top,top+1)
                union(parent,top+2,top+3)
            if val in ['\\',' ']:
                union(parent,top,top+2)
                union(parent,top+1,top+3)

            if(r+1<n):
                union(parent,top+3+5*r,top+8+5*r)
            if(c+1<n):
                union(parent,top+2+8*c,top+5+8*c)
    return sum(parent[x]==x for x in range(4*n*n))

grid=[]
for i in range(4):
    inp=input()
    if(i==1 or i==2):
        l=list(inp[3:5])
        grid.append(l)
print(union_find(grid))


