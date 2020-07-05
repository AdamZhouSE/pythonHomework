nums=list(map(int,input().split(',')))
i=1
while i<len(nums)-1:
    if nums[i-1]<nums[i] and nums[i]>nums[i+1]:
        print(i)
        break
    else:
        i+=1
if i==len(nums)-1:
    if nums[0]>nums[1]:
        print(0)
    else:
        print(len(nums)-1)