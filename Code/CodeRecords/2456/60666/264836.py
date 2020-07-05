nums=eval(input())
counts=[]
for i in range(len(nums)-1):
    count=0
    for j in range(i,len(nums)):
        if nums[j]<nums[i]:
            count+=1
    counts.append(count)
counts.append(0)
print(counts)