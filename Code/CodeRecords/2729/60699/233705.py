str=input()
a=(len(str)-1)
str=str[1:a]
nums=list(map(int,str.split(",")))
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