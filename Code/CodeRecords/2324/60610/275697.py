nums=list(map(int,input().split(",")));
k=int(input());
a=min(nums)+k;
b=max(nums)-k;
for i in range(len(nums)):
    if(abs(nums[i]+k-a)<abs(nums[i]-k-a)):
        nums[i]+=k;
    else:
        nums[i]-=k;
print(max(nums)-min(nums))