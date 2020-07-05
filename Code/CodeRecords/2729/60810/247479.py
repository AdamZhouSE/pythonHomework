inp = input()
nums = inp[1:len(inp)-1].split(",")
lo = 0
hi = len(nums) - 1
while lo < hi:
    mid = lo + (hi - lo) // 2
    if mid % 2 == 1:
        mid -= 1
    if nums[mid] == nums[mid + 1]:
        lo = mid + 2
    else:
        hi = mid
print(nums[lo])