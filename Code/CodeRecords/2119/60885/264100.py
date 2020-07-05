def isCross(nums):
    if len(nums) < 4:
        return False
    a,b,c,(d,e,f) = 0,0,0,nums[:3]
    for i in range(3, len(nums)):
        a,b,c,d,e,f = b,c,d,e,f,nums[i]
        if e < c - a and f >= d:
            return True
        if c - a <= e <= c and f >= -abs(d-b):
            return True
    return False

nums = eval(input())
print(isCross(nums))