nums=eval(input())
result=[]
for i in range(len(nums)):
    n=0
    for j in range(i,len(nums)):
        if(nums[j]<nums[i]):
            n+=1
    result.append(n)
print(result)