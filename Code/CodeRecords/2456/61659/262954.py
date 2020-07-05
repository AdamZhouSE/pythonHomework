nums=eval(input())
counts=[]
for i in range(0,len(nums)):
    count=0
    for j in range(i,len(nums)):
        if nums[j]<nums[i]:
            count=count+1
    counts.append(count)
print(counts)