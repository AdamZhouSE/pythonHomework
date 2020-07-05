arr = eval(input())

def firstMissingPositive(nums):
    if 1 not in nums:
        return 1
 
    n = len(nums)
    if n == 1:
        return 2
    
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = 1
    
    for num in nums:
        if abs(num) == n:
            if nums[0] > 0:
                nums[0] = -nums[0]
        else:
            if nums[abs(num)] > 0:
                nums[abs(num)] = -nums[abs(num)]
    
    for i in range(1, n):
        if nums[i] > 0:
            return i
    
    if nums[0] > 0:
        return n
    else:
        return n + 1

print(firstMissingPositive(arr))
