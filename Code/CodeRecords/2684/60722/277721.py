T=int(input())
for m in range(T):
    N=int(input())
    nums=input().split(" ")
    for i in range(N):
        nums[i]=int(nums[i])
    result=[]
    def DFS(count,i):
        if i==N-2 or i==N-1:
            result.append(count)
            return
        else:
            DFS(count+nums[i+1],i+1)
            DFS(count+nums[i+2],i+2)
    DFS(nums[0],0)
    DFS(nums[1],1)
    result.sort()
    print(result[0])