s=eval(input())
nums=list(map(int,input().split(",")))
length=len(nums)

slow=0
fast=-1
result=length+1
sum=0
while slow<length:
    if sum<s:
        fast+=1
        if fast<length:
            sum+=nums[fast]
        else:
            break
    else:
        result=min(result,fast-slow+1)
        sum-=nums[slow]
        slow+=1
print(result if result!=length+1 else 0)
