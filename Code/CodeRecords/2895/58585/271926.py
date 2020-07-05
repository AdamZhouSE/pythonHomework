source=input()
nums=[0 for x in range(2)]
nums[0]=int(source[1])
nums[1]=int(source[3])
init=nums[0]
for i in range(nums[0]+1,nums[1]+1):
    init=init&i
print(init)
