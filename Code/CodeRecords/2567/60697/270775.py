nums=eval(input())
low=int(input())
high=int(input())
count=0
for i in range(len(nums)):
    ans=0
    for j in range(i,len(nums)):
        ans+=nums[j]
        if(ans>=low and ans<=high):
            count+=1
print(count)