def func(nums,sum):
    n=len(nums)
    dp2=[float("+inf")]*n
    dp=[2**31-1]*n
    for i in range(n-1,-1,-1):
        tmpsum=0
        for j in range(i,n):
            tmpsum+=nums[j]
            if tmpsum>=sum:
                dp[i]=j-i+1
                break
    return min(dp)
sum=int(input())
nums=eval("["+input()+"]")
print(func(nums,sum))

