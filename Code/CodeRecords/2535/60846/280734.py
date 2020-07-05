#思路巧妙  因为数字是0 1 2 。。。n的排列
def maxChuncksToMakeSorted(nums):
    ma=0
    ret=0
    for i in range(len(nums)):
        ma=max(ma,nums[i])
        if ma==i: ret+=1
    return ret
print(maxChuncksToMakeSorted(eval(input())))