nums=eval(input())
result=0
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i]>2*nums[j]:
            result+=1
print(result)