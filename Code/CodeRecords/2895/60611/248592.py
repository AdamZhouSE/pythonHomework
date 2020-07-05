nums = list(map(int,input()[1:-1].split(",")))
length=nums[1]-nums[0]
result=0
for i in range(1,length):
    result=int(nums[0] & nums[0]+i)
print(result)