nums=eval(input())
lower=eval(input())
upper=eval(input())
count=0
for i in range(0,len(nums)):
    temp=0
    for j in range(i,len(nums)):
        for k in range(i,j+1):
            temp+=nums[k]
        if (temp>=lower)&(temp<=upper):
            count+=1
print(count)