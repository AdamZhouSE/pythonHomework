nums = eval(input())
left = 0
right = len(nums)-1
while True:
    if left == right:
        break
    elif nums[left] <= min(nums[left+1:]):
        left += 1
        continue
    else:
        break
while True:
    if right == left:
        break
    elif nums[right] >= nums[right-1]:
        right -= 1
    else:
        break
print(right-left+1)
