nums = list(map(int, input()[1:-1].split(",")))
left = 0
right = len(nums)-1
while left < right:
    while nums[left]%2 == 0 and left<right:
        left += 1
    while nums[right]%2 == 1 and right > left:
        right -= 1
    temp = nums[left]
    nums[left] = nums[right]
    nums[right] = temp
print(nums)
