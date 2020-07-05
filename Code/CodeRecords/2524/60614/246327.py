input()
nums=[int(x) for x in input().split()]
judge=True
def check(nums):
    if len(nums)>1:
        left=[]
        right=[]
        for i in range(1,len(nums)):
            if nums[i]<nums[0]:
                left.append(nums[i])
            else:
                right.append(nums[i])
        return [nums[0]]+check(left)+check(right)
    else:
        return nums
print(check(nums))