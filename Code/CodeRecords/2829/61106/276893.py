n=int(input())
nums=input().split()
if n==2:
    print(0)
else:
    for i in range(len(nums)):
        nums[i]=int(nums[i])
    nums.sort()
    if nums[-1]-nums[1]>nums[-2]-nums[0]:
        del nums[-1]
    else:
        del nums[0]
    print(nums[-1]-nums[0])