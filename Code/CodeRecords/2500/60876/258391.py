nums=eval(input())
right=sorted(nums)
result=[]
length=len(nums)
index=len(nums)-1
while nums != right:
    while nums[index] == right[index]:
        index -= 1
    temp1 = nums[0:index+1]
    temp2 = nums[index+1:length]
    temp=nums.index(right[index])
    if temp!=0:
        result.append(temp+1)
    nums=temp1[0:temp+1]
    temp12=temp1[temp+1:index+1]
    nums=nums[::-1]
    nums.extend(temp12)
    nums=nums[::-1]
    nums.extend(temp2)
    result.append(index+1)
print(result)