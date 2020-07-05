#Leetcode329 记忆化搜索\
inp=''
temp=input()
while(temp!=']'):
    inp+=temp
    temp=input()
nums=eval(inp+']')
m=len(nums[0])
n=len(nums)
cache=[[0 for i in range(m)] for j in range(n)]
dir=[[0,1],[1,0],[-1,0],[0,-1]]
def Maxdis(nums,cache,dir,m,n):
    ans=0
    for i in range(n):
        for j in range(m):
            ans=max(ans,dfs(i,j,cache,dir,n,m))
    return ans
def dfs(i,j,cache,dir,n,m):
    if cache[i][j]!=0:
        return cache[i][j]
    else:
        for k in range(len(dir)):
            x = i + dir[k][0]
            y = j + dir[k][1]
            if x>=0 and x<n and y>=0 and y<m and nums[i][j]<nums[x][y]:
                cache[i][j]=max(cache[i][j],dfs(x,y,cache,dir,n,m))
        cache[i][j]=cache[i][j]+1
        return  cache[i][j]
print(Maxdis(nums,cache,dir,m,n))