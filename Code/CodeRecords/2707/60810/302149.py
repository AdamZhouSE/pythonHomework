n=input()
nums=n[1:-1].split(", ")
res=0
i=0
for m in range(len(nums)):
    nums[m]=int(nums[m])
while(i<len(nums)):
    if(nums[i]%2==0):
        if(nums[i+1]==nums[i]+1):
            i+=2
            continue
        else:
            for j in range(i,len(nums)):
                if(nums[j]==nums[i]+1):
                    res+=1
                    temp=nums[i+1]
                    nums[i+1]=nums[i]+1
                    nums[j]=temp
                    i+=2
                    break
    else:
        if(nums[i+1]==nums[i]-1):
            i+=2
            continue
        else:
            for j in range(i,len(nums)):
                if(nums[j]==nums[i]-1):
                    res+=1
                    temp=nums[i+1]
                    nums[i+1]=nums[i]-1
                    nums[j]=temp
                    i+=2
                    break
print(res)