nums=list(map(int,input().split(",")))
re=[0 for x in range(len(nums))]
re[0]=nums[0]
for i in range(1,len(nums)): 
    re[i]=max(re[i-1]+nums[i],nums[i]) 

result=re[0]
for i in range(1,len(re)):
    result=max(result,re[i])
               
print(result)