nums=eval(input())
lower=int(input())
upper=int(input())
cnt=0
for i in range(len(nums)):
    for j in range(i,len(nums)):
        if lower<=sum(nums[i:j+1])<=upper:
            cnt+=1
print(cnt)