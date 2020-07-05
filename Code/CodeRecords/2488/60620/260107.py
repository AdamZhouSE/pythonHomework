nums=eval(input())
nums=sorted(nums)
result=[]
for i in range(len(nums)//2):
    result.append(nums[i])
    result.append(nums[len(nums)-i-1])
if(len(nums)%2==1):
    result.append(nums[len(nums)//2])
print(result)