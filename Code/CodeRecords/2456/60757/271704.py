nums=eval(input())
counts=[]
for i in range(len(nums)-1):
    count=0
    for j in range(i+1,len(nums)):
        if nums[j]<nums[i]:
            count=count+1
    counts.append(count)
counts.append(0)
print(counts)