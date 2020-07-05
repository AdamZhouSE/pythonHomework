nums=eval(input())
lower=int(input())
upper=int(input())
count=0
for i in range(0,len(nums)):
    for j in range(i,len(nums)):
        sum1=sum(nums[i:j+1])
        if(sum1<=upper and sum1>=lower):
            count+=1
print(count)