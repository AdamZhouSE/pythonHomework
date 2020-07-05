nums = list(map(int, input()[1:-1].replace(" ", "").split(",")))
sort = sorted(list(nums))
length = len(nums)
left = 0
while left < length:
    if nums[left] == sort[left]:
        left += 1
    else:
        break
right = length - 1
while right >= 0:
    if nums[right] == sort[right]:
        right -= 1
    else:
        break
if right == -1:
    print(0)
else:
    print(right-left+1)
