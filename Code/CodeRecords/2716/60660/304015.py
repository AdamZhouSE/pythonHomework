import re
def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(x, y):
    xr = find(x)
    yr = find(y)
    p[xr] = yr
input()
row=str(re.findall('\"(.*)\"', input())[0])
row=row.replace('\\\\','\\')
print(row)
grid=[]
while(row!=']'):
    grid.append(row)
    try:
        row=str(re.findall('\"(.*)\"', input())[0])
        row=row.replace('\\\\', '\\')
    except:
        row=']'
n=len(grid)
p=[i for i in range(n*n*4)]
for r, row in enumerate(grid):
    for c, val in enumerate(row):
        root = 4 * (r*n + c)
        if val in '/ ':
            union(root + 0, root + 1)
            union(root + 2, root + 3)
        if val in '\ ':
            union(root + 0, root + 2)
            union(root + 1, root + 3)

        # north/south
        if r+1 < n: union(root + 3, (root+4*n) + 0)
        if r-1 >= 0: union(root + 0, (root-4*n) + 3)
        # east/west
        if c+1 < n: union(root + 2, (root+4) + 1)
        if c-1 >= 0: union(root + 1, (root-4) + 2)
ans=0
for i in range(len(p)):
    if p[i]==i:
        ans+=1
print(ans)
