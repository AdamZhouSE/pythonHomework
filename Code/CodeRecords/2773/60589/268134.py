from sys import stdin
mtrx=stdin.readlines()
mtrx.pop()
mtrx.pop(0)
for i in range(len(mtrx)-1):
    mtrx[i]=eval(mtrx[i][:-2].strip())
mtrx[-1]=eval(mtrx[-1][:-1].strip())
directions=((-1,0),(1,0),(0,-1),(0,1))
m = len(mtrx)
n = len(mtrx[0])
memorized=[[0]*n]*m #记忆化 减少时间复杂度


def longest_path():
    global m
    global n
    if len(mtrx)==0:
        return 0
    ans=0
    for i in range(m):
        for j in range(n):
            ans=max(ans,dfs(i,j))
    if ans==2:
        ans=4
    return ans


def dfs(i,j):
    if memorized[i][j]!=0:
        return memorized[i][j]
    for d in directions:
        new_i=i+d[0]
        new_j=j+d[1]
        if 0 <= new_i < m and 0 <= new_j < n and mtrx[new_i][new_j]>mtrx[i][j]:
            memorized[i][j]=max(memorized[i][j],dfs(new_i,new_j))
    memorized[i][j]+=1
    return memorized[i][j]


print(longest_path())