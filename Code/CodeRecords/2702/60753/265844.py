import sys
import re
import math
def dfs(maps,i,j):
    if i<0 or i>=len(maps) or j<0 or j>=len(maps[0]) or maps[i][j]!=1:
        return
    else:
        maps[i][j]=2
        dfs(maps,i-1,j)
        dfs(maps,i+1,j)
        dfs(maps,i,j+1)
        dfs(maps,i,j-1)        
s=sys.stdin.read()
strlist=s.split("\n")
m=len(strlist[0])
n=len(strlist)
maps=[[0]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        maps[i][j]=int(strlist[i][j])
count=0
for i in range(n):
    for j in range(m):
        if maps[i][j]==1:
            count+=1
            dfs(maps,i,j)
print(count)