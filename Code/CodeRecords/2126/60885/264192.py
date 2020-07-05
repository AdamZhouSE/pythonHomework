def valid(nums):
    for i in range(len(nums)-1):
        for j in range(1, len(nums)):
            if not(nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0):
                return False
    return True

def find_max_sub(nums):
    if valid(nums):
        return nums
    result = []
    for i in range(len(nums)):
        temp = nums.pop(-1-i)
        pos = find_max_sub(nums.copy())
        if len(pos) > len(result):
            result = pos
        nums.append(temp)
    return result

nums = list(map(int, input().split(',')))
result = find_max_sub(nums)
print(result)