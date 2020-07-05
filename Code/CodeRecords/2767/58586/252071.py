nums=int(input())
for i in range(nums):
    num=int(input())
    arr=[3,5,10]
    def backtrack(start,ans,temp):
        if temp==num:
            ans[0]+=1
            return
        if temp>num:
            return
        for i in range(start,len(arr)):
            temp+=arr[i]
            backtrack(i,ans,temp)
            temp-=arr[i]
    ans=[0]
    backtrack(0,ans,0)
    print(ans[0])