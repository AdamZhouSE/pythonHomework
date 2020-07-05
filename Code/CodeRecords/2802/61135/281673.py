nm=input().split(" ")
n=int(nm[0])
m=int(nm[1])
nums=input().split(" ")
nums=list(int(a) for a in nums)
res=0
while(True):
    count=0
    for a in range(0,n):
        if(nums[a]<=m):
            if(nums[a]!=0):
                nums[a]=0
                res=a+1
                count=count+1
        else:
            nums[a]=nums[a]-m
            count=count+1
    if(count==0):
        break;
print(res)
    
    
        
    
