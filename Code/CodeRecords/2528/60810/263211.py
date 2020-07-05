'''
给定一个整数数组 nums，将该数组升序排列
'''

inp = input()
nums = inp[1: len(inp) - 1].split(",")
for i in range(1, len(nums)):
    for j in range(i,0,-1):
        if nums[j] < nums[j-1]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
        else:
            break
nums = list(map(int, nums))
print(nums)