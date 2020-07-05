nums=input()[1:-1].split(",")
i=len(nums)-1
while i>=0:
    if nums[i] not in nums[0:i]:
        print(nums[i])
        break
    i=i-1