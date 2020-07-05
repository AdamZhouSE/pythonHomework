def count(nums):
    idx = nums.index(max(nums))
    ans = 0
    if len(nums) == 1:
        return 0
    if idx + 1 < len(nums):
        ans += nums[idx] + count(nums[idx + 1:])
    if 0 <= idx - 1:
        ans += nums[idx] + count(nums[:idx])
    return ans


ns = int(input())
lst = []
for n in range(ns):
    lst.append(int(input()))
print(count(lst))
