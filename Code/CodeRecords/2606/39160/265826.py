nums = eval(input())
target = int(input())

left, right = 0, len(nums) - 1
res = -1

while left <= right:
    pivot = left + (right - left) // 2
    if nums[pivot] == target:
        res = pivot
    if target < nums[pivot]:
        right = pivot - 1
    else:
        left = pivot + 1

print(res)