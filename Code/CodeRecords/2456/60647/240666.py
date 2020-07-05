nums=input()
counts=[]
for i in range(len(nums)):
    counts.append(0)
for i in range(len(nums)-1):
    for j in range(i,len(nums)):
        if nums[j]<nums[i]:
            counts[i]=counts[i]+1
print(counts)