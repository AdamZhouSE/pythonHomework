nums = eval(input())
target = eval(input())
start = 0
end = len(nums) - 1
mid = (start + end) // 2
res = -1
while start <= end:
    if target == nums[mid]:
        res = mid
        break
    elif target < nums[mid]:
        end = mid - 1
    else:
        start = mid + 1
    mid = (start + end) // 2
print(res)