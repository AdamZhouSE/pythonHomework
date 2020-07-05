def judge(nums):
    res=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)+1):
            temp=nums[i:j]
            res=sum(temp)
            if res==0:
                return "Yes"
    return "No"

if __name__=="__main__":
    tests=int(input())
    for _ in range(tests):
        n=int(input())
        nums=input().split()
        nums=[int(x) for x in nums]
        ans=judge(nums)
        print(ans)