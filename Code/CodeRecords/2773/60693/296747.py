dir=[[0,1],[1,0],[0,-1],[-1,0]]


def dfs(arr,i,j,cache):
    if cache[i][j]:return cache[i][j]
    for d in dir:
        x,y=i+d[0],j+d[1]
        if 0<=x<len(arr) and 0<=y<len(arr[0]) and arr[x][y]>arr[i][j]:
            cache[i][j]=max(cache[i][j],dfs(arr,x,y,cache))
    cache[i][j]+=1
    return cache[i][j]


def longestIncreasingPath(arr:[[int]]):
    if not len(arr):return 0
    m,n=len(arr),len(arr[0])
    cache=[[0 for i in range(n)] for j in range(m)]
    res=0
    for i in range(m):
        for j in range(n):
            res=max(res,dfs(arr,i,j,cache))
    return res


inp=input()
arr=[]
inp=input()
while inp!=']':
    row=eval(inp[:len(inp)-1]) if inp[-1]==',' else eval(inp)
    arr.append(row)
    inp=input()
print(longestIncreasingPath(arr))