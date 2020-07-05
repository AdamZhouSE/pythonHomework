nums=eval(input())
lower=int(input())
upper=int(input())
length=len(nums)
result=0
for start in range(0,length):
    sum=0
    for end in range(start,length):
        sum+=nums[end]
        if sum>=lower and sum<=upper:
            result+=1
print(result)