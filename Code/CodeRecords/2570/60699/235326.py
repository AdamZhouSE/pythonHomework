from bisect import bisect_left

cnt=int(input())
arr=[]
for i in range(0,cnt):
    temp=input()
    temp=list(map(int,temp.split(',')))
    arr.append(temp)
arr.sort(key=lambda x: (x[0], -x[1]))

def lis(nums):
    dp = []
    for i in range(len(nums)):
        idx = bisect_left(dp, nums[i])
        if idx == len(dp):
            dp.append(nums[i])
        else:
            dp[idx] = nums[i]
    return len(dp)
print(lis([i[1] for i in arr]))