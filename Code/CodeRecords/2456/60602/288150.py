nums=eval(input());
i=0;
ans=[];
while(i<len(nums)):
    count=0;
    j=i+1;
    while(j<len(nums)):
        if(nums[i]>nums[j]):
            count+=1;
        j+=1;
    ans.append(count);
    i+=1;

print(ans);