nums=eval(input())
lower=int(input())
upper=int(input())
res=0
for i in range(len(nums)):
    for j in range(i+1,len(nums)+1):
        s=sum(nums[i:j])
        if s>=lower and s<=upper:
            res+=1
print(res)