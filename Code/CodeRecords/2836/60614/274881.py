length=int(input())
nums=[int(x) for x in input().split()]
destination=sorted(nums)
count=0
while nums!=destination:
    if nums[len(nums)-1]>nums[0]:
        count=-1
        break
    else:
        nums=[nums[len(nums)-1]]+nums[0:len(nums)-1]
        count+=1
print(count)