nums=eval(input())
lower,upper=int(input()),int(input())
count=0
for i in range(len(nums)):
    for j in range(i+1,len(nums)+1):
        if lower<=sum(nums[i:j])<=upper:
            count+=1
print(count)