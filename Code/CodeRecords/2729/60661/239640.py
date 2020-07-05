nums=input()[1:-1].split(',')
nums=[int(x) for x in nums]
mid=int(len(nums)/2)
while mid!=0 and mid!=len(nums)-1 and (nums[mid]==nums[mid+1] or nums[mid]==nums[mid-1]) :
    if (len(nums)+1)%4!=0:
        if nums[mid]==nums[mid-1]:
            nums=nums[:mid-1]
        else:
            nums=nums[mid+2:]
        mid = int(len(nums) / 2)
    else:
        if nums[mid] == nums[mid + 1]:
            nums = nums[:mid]
        else:
            nums = nums[mid + 1:]
        mid = int(len(nums) / 2)
print(nums[mid])