num=int(input())
nums = list(map(int, str(num)))
i = 0
while i < len(nums):
    target = nums[i]
    idx = i
    for j in range(len(nums) - 1, i, -1):
        if nums[j] > target:
            target = nums[j]
            idx = j
    if nums[i] != target:
        nums[i], nums[idx] = nums[idx], nums[i]
        break
    i += 1
res= int("".join(map(str, nums)))
print(res)
