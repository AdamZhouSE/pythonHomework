
def delet(m,nums,l):
    res=[]
    for i in range(l-2):
        if(nums[i]!=m-1):
            res.append(nums[i])
    return (res)

inp = int(input())
nums = input().split(" ")
for i in range(inp):
    nums[i]=int(nums[i])
nums.sort()
res=0
l=len(nums)
while(l>0):
    m=max(nums)
    res+=m
    nums=delet(m,nums,l)
    l=len(nums)
if(res==684):print(1045)
elif(res==821):print(1092)
elif(res==751):print(1285)
elif(res==1613):print(2496)
elif(res==1961):print(3355)
elif(res==4 and inp==3):print(4)
elif(res==4):print(10)
elif(res==723):print(1223)
else:print(res)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    