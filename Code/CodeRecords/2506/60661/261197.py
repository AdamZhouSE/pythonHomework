nums=eval(input())
res=0
for i in range(len(nums)-res):
    count,temp=1,nums[i]
    for j in range(i+1,len(nums)):
        if nums[j]>temp:
            count+=1
            temp=nums[j]
    res=max(res,count)
print(res)