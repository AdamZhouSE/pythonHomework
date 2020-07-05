res=False
def dp(l,p,target,nums):
    if target==0:
        global res
        res=True
        return
    elif l==0 or target<0:
        return
    for i in range(p,len(nums)+1-l):
        dp(l-1,p+1,target-nums[i],nums)

nums=eval(input())
total=sum(nums)
average=total/len(nums)
if average in nums:
    print(True)
    exit()
for l in range(2,len(nums)):
    target=average*l
    dp(l,0,target,nums)
    if res:
        print(True)
        exit()
print(False)