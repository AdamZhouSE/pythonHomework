import bisect
def LIS(nums):
    dp=[]
    for i in range(len(nums)):
        index=bisect.bisect_left(dp,nums[i])
        if index==len(dp):
            dp.append(nums[i])
        else:
            dp[index]=nums[i]
    return len(dp)
n=int(input())
envelopes=[]
for i in range(n):
    envelopes.append(list(map(int,input().split(","))))
envelopes.sort(key=lambda  x:(x[0],-x[1]))
arr=[]
for i in envelopes:
    arr.append(i[1])
print(LIS(arr))