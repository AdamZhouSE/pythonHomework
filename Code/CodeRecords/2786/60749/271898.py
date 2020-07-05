n=int(input())
ans=list(map(int,input().split(" ")))
def maxdays(nums):
    nums=sorted(nums)
    days=0
    for t in range(len(nums)):
        if nums[t]>=t+1:
            days+=1
        else:
            return days
print(maxdays(ans))