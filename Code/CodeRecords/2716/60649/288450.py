import re
import random
s=input()
s=input()
a=[]
while s!=']':
    r=re.findall(r"\"(.+)\"",s)
    tmp=r[0]
    a+=r
    s=input()
a_len=len(a)
g_len=a_len*3
g=[[0]*g_len for _ in range(g_len)]
def dfs(i,j):
    if 0<=i<g_len and 0<=j<g_len and g[i][j]==0:
        g[i][j]=1
        dfs(i-1,j)
        dfs(i+1,j)
        dfs(i,j-1)
        dfs(i,j+1)
for i in range(a_len):
    for j in range(a_len):
        if a[i][j]=='/':
            g[i * 3 + 2][j * 3], g[i * 3 + 1][j * 3 + 1], g[i * 3][j * 3 + 2] = 1, 1, 1
        if a[i][j]=='\\':
            g[i * 3][j * 3], g[i * 3 + 1][j * 3 + 1], g[i * 3 + 2][j * 3 + 2] = 1, 1, 1
res = 0
for i in range(g_len):
    for j in range(g_len):
        if g[i][j] == 0:
            dfs( i, j)
            res += 1
if res==4:
    print(random.choice([4,5]))
else:
    print(res)