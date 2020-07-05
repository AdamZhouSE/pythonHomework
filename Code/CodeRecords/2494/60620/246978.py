nums=eval(input())
result=0
for i in range(len(nums)):
    for j in range(i,len(nums)):
        if(nums[i]>2*nums[j]):
            result+=1
print(result)
    