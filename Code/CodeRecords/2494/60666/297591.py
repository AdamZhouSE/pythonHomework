nums=eval(input())
count=0
for i in range(len(nums)):
    for j in range(i,len(nums)):
        if nums[i]>2*nums[j]:
            count+=1
print(count)