import sys
import re
import math
d=((0,1),(1,0),(-1,0),(0,-1))
m=0
n=0
flag=[]
def dfs(matrix,i,j):
    if flag[i][j]!=0:
        return flag[i][j]
    else:
        for (x,y) in d:
            x,y=i+x,j+y
            if x>=0 and x<m and y>=0 and y<n and matrix[x][y]>matrix[i][j]:
                flag[i][j]=max(flag[i][j],dfs(matrix,x,y))
        flag[i][j]+=1
        return flag[i][j]
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
sli=s.split("\n")
m=len(sli)-2
n=len(nums)//m
flag=[[0 for i in range(n)] for j in range(m)]
matrix=[[0 for i in range(n)] for j in range(m)]
for i in range(m):
    for j in range(n):
        matrix[i][j]=nums[i*m+j]
res_max=0
for i in range(m):
    for j in range(n):
        res_max=max(res_max,dfs(matrix,i,j))
print(res_max)
