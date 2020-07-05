inp=input().split(" ")
N=int(inp[0])
M=int(inp[1])
result=0
res=[[0 for i in range(0,N)]for j in range(0,N)]
for i in range(0,M):
    nums=input().split(" ")
    nums=list(int(x) for x in nums)
    res[nums[0]-1][nums[1]-1]=1
for i in range(N):
    for j in range(N):
        if(res[j][i]==1):
            for k in range(N):
                res[j][k]=res[j][k] | res[i][k]
for i in range(N):
    mid=0
    for j in range(N):
        if res[j][i]==1 and j!=i:
            mid=mid+1
    if mid==N-1:
        result=result+1
print(result)