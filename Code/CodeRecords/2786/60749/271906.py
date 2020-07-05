n=int(input())
ans=list(map(int,input().split(" ")))
def maxdays(nums):
    nums=sorted(nums)
    days=0
    a=1
    for t in range(len(nums)):
        if nums[t]>=a:
            days+=1
            a+=1


    return days
print(maxdays(ans))