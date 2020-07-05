nums = input()
nums = nums.replace('[','')
nums = nums.replace(']','')
nums = nums.split(',')
size = len(nums)
left = 1
right = size - 1
while left < right:
    mid = (left + right) >> 1
    cnt = 0
    for num in nums:
        if num <= mid:
            cnt += 1
        if cnt > mid:
            right = mid
        else:
            left = mid + 1
print(left)