nums = eval(input())
numk = nums.copy()
numk.sort()
ls = len(nums)
l = 0
r = 0
for i in range(ls):
    if nums[i]!=numk[i]:
        l = i
        break
for i in range(ls-1,0,-1):
    if nums[i]!=numk[i]:
        r = i
        break
c = r - l + 1
print(c)