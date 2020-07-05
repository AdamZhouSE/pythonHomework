nums = eval('['+input()+']')
def do(nums):
    if nums[0]> nums[1]:
        return 0
    else:
        try:
            for i in range(1, len(nums) - 1):
                if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                    result = i
                    break
            return result
        except Exception as e:
            return  len(nums) - 1

print(do(nums))