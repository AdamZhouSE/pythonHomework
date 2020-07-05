nums=eval(input())
counts=[]
for i in range(0,len(nums)-1):
    count=0
    for j in range(i+1,len(nums)):
        if(nums[i]>nums[j]):
            count+=1
    counts.append(count)
counts.append(0)
print(counts)