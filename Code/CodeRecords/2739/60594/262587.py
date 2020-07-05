
def dfs(res,tmp,nums,s,n,k):
    if n == 0 and len(tmp) == k:
        q=[]
        for index in tmp:
            q.append(index)
        res.append(q)
    elif n>=0 and len(tmp)<k:
        for i in range(s,len(nums)):
            tmp.append(nums[i])
            dfs(res,tmp, nums, i+1, n-nums[i], k)
            tmp.pop()
res=[]
s=input()
k=(int)(s[0])
n=(int)(s[3])
nums=[1,2,3,4,5,6,7,8,9]
dfs(res,[],nums,0,n,k)
print(res)