
def search(nums: list):
    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return min(nums[0],nums[1])

    R = len(nums) - 1
    L = 0
    M = (R + L) // 2
    while True:
        if nums[M-1] < nums[M] < nums[M+1]:
            return min(search(nums[0:M]), search(nums[M+1:len(nums)]))
        elif nums[M+1] < nums[M]:
            return nums[M+1]
        elif nums[M-1] > nums[M]:
            return nums[M]

nums = [int(x) for x in input().split(',')]
print(search(nums))