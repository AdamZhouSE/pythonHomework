nums=int(input())
for i in range(nums):
    src=list(map(int,input().split(" ")))
    def dfs(src,temp,ans,start,depth):
        if depth==0 and len(temp)==src[1]:
            ans[0]+=1
            return
        for i in range(start,src[0]//pow(2,depth-1)+1):
            temp.append(i)
            dfs(src,temp,ans,i*2,depth-1)
            temp.pop()
    ans=[0]
    dfs(src,[],ans,1,src[1])
    print(ans[0])