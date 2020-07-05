
def optimalDivision(nums):
    if len(nums) > 2:
        return str(nums[0]) + '/(' + '/'.join([str(i) for i in nums[1:]]) + ')'
    else:
        return str(nums[0]) + (('/' + str(nums[1])) if len(nums) == 2 else '')


nums=[int(x) for x in input().split(',')]
print(optimalDivision(nums))