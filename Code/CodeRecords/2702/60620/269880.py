import sys
r=[]
num=1
while True:
    s = sys.stdin.readline().strip()
    if(s==''):
        break
    else:
        s=list(s)
        r.append(s)
row=len(r)
col=len(r[0])
num=0
def dfs(i, j):
    r[i][j] = '0'
    for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        a=i+x
        b=j+y
        if 0<=a<row and 0<=b<col and r[a][b]=='1':
            dfs(a, b)
for i in range(row):
    for j in range(col):
        if r[i][j]=='1':
            dfs(i, j)
            num+= 1
print(num)
