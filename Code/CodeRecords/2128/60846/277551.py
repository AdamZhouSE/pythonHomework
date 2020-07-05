def maxf(nums):
    s=sum(nums)
    n=len(nums)
    f=[]
    tmp=0
    for i in range(n):
        tmp+=i*nums[i]
    f.append(tmp)
    for i in range(1,n):
        f.append(f[-1]+s-n*nums[n-i])
    return max(f)
print(maxf(eval("["+input()+"]")))