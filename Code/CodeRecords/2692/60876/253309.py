import math
nums=eval(input())
temp=nums.copy()
days=int(input())
sum=0
for item in nums:
    sum+=item
min=math.ceil(sum/days)
day=[]
if nums[len(nums)-1]>min:
    min=nums[len(nums)-1]
while True:
    sum=0
    for i in range(0,days):
        while nums!=[] and sum+nums[0]<=min:
            sum+=nums[0]
            del nums[0]
        sum=0
    if nums!=[]:
        min += 1
        del day
        day = []
        del nums
        nums = temp.copy()
    else:
        break
print(min)