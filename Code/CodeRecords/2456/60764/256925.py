nums=eval(input())
res=[]
for i in range(len(nums)-1):
    count=0
    for j in range(i+1,len(nums)):
        if nums[j]<nums[i]:
            count+=1
    res.append(count)
res.append(0)
print(res)