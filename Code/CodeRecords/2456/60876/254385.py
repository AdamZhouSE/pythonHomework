nums=eval(input())
result=[]
sum=0
for i in range(0,len(nums)):
    sum=0
    for j in range(i+1,len(nums)):
        if nums[j]<nums[i]:
            sum+=1
    result.append(sum)
print(result)