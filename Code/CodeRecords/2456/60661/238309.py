nums=input()[1:-1].split(',')
nums=[int(x) for x in nums]
count=[]
for i in range(len(nums)-1):
    temp=nums[i:]
    temp.sort()
    count.append(temp.index(nums[i]))
count.append(0)
print(count)