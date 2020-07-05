nums=[]
result=[]
for i in range(0,3):
    nums.append(input())
list.sort(nums)
min=(int)(nums[0])
mid=(int)(nums[1])
max=(int)(nums[2])
if(max-min==2):
    result.append(0)
elif((mid-min<=2)|(max-mid<=2)):
    result.append(1)
else:
    result.append(2)

result.append(max-min-2)
print(result)