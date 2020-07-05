def splitArray(nums,m):
    left = max(nums)
    right = sum(nums)

    def helper(mid):
        cur = 0
        res = 1
        for num in nums:
            cur += num 
            if cur > mid:
                res += 1
                cur = num 
        return res 
    while left < right:
        mid = (left + right) // 2
        if helper(mid) > m:
            left = mid + 1
        else:
            right = mid
    return left
a=input().split(',')
a=[int(x) for x in a]
b=int(input())
print(splitArray(a,b))