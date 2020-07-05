nums=list(input())
target=int(input())
if target in nums:
    
    for x in range(0, len(nums)):
        if nums[x]==target:
            print(x)
else:
    if target>nums[len(nums)-1]:
        print(len(nums))
    if target<nums[0]:
        print(0)
    for x in range(0, len(nums)-1):
        if target>nums[x] and target<nums[x+1]:
            print(x+1)
