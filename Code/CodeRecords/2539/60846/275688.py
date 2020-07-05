def sortLen(nums):
    i=0
    while i<len(nums) and nums[i]<nums[i+1]:
        i+=1
    if i==len(nums): return 0
    
    j=len(nums)-1
    while j>0 and nums[j-1]<nums[j]:
        j-=1
    return j-i+1
print(sortLen(eval(input())))