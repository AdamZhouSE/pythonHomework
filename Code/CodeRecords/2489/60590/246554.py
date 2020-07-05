nums=input()[1:-1].split(',')
nums=[int(x) for x in nums]
lower=int(input());upper=int(input())
count=0
for i in range(len(nums)):
    for j in range(i,len(nums)):
        temp=nums[i:j+1]
        if upper >= sum(temp) >= lower:
            count+=1
print(count)