import re
x=int(input())
list=[]
for i in range(0,x):
    nums=re.findall(r"[0-9]{1,}",input())
    nums=[int(l) for l in nums]
    list.extend(nums)
nums=list
p=True
k=(nums[1]-nums[3])/(nums[0]-nums[2])
b=nums[1]-k*nums[0]
for i in range(5,len(nums),2):
    if((nums[i])!=(k*nums[i-1]+b)):
        p=False
print(p)