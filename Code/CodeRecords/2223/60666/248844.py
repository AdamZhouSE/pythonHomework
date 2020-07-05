nums=list(map(int,input().strip().split(",")))
nums.sort()
for i in range(len(nums)-1):
    if nums[i]==nums[i+1]:
        repeat=nums[i]
        break
lst=[]
for number in range(len(nums)):
    lst.append(number)
for num in lst:
    if num in nums:
        pass
    else:
        loss=num
print("["+str(repeat)+", "+str(loss)+"]")