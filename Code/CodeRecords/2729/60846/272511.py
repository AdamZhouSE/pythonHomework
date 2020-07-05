def findWordAppearingOnce(nums):
    ret=0
    for num in nums:
        ret=ret^num
    return ret
nums=eval(input())
print(findWordAppearingOnce(nums))