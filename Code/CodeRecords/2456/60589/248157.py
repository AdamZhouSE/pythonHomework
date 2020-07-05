nums=input()[1:-1].split(',')
nums=list(map(int,nums))
counts=[]
for i in range(len(nums)):
    a=nums[i]
    n=0
    for j in range(i+1,len(nums)):
        if nums[j]<a:
            n+=1
    counts.append(n)
print(counts)