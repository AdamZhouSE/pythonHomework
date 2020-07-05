def splitArray(nums,m):
    left = 0
    right = 0
    length = len(nums)
    for i in range(0,length):
        right += nums[i]
        if(left<nums[i]):
            left = nums[i]
    res = right
    while(left<=right):
        mid = int((left+right)/2)
        sum = 0
        cnt = 1
        for i in range (0,length):
            if(nums[i]+sum>mid):
                cnt += 1
                sum = nums[i]
            else:
                sum += nums[i]
        if(cnt<=m):
            res = min(res,mid)
            right = mid - 1
        else:
            left = mid + 1
    return res

inp = input().split(",")
nums = []
for i in inp:
    nums.append(int(i))
m = int(input())
print(splitArray(nums,m))