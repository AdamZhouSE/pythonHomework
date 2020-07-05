nums=input().split(",")
nums[0]=nums[0][1:len(nums[0])]
nums[-1]=nums[-1][0:-1]
result=[]
for i in nums:
    if nums.count(i)>len(nums)//3:
        if int(i) not in result:
            result.append(int(i))
print(result)
