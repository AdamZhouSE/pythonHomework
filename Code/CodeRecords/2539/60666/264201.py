nums=eval(input())
if sorted(nums)==nums:
    print(0)
else:
    newNums=sorted(nums)
    for i in range(len(nums)):
        if nums[i]!=newNums[i]:
            break
    for j in range(len(nums)-1,-1,-1):
        if nums[j]!=newNums[j]:
            break
    result=max(j-i+1,0)
    print(result)