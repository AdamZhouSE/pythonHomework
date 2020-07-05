nums=[int(i) for i in input()[1:-1].split(",")]
nums_ordered=list()
nums_ordered = sorted(nums)
r=-1
l=len(nums)
for i in range(len(nums)):
    if nums_ordered[i]!=nums[i]:
        l = i
        break
for i in range(len(nums)-1,0,-1):
    if nums_ordered[i]!=nums[i]:
        r = i
        break
if r <= l:
    print(0)
else:
    print(r - l + 1)