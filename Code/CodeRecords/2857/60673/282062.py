
inp = int(input())
nums=input().split(" ")
res=0
for i in range(inp):
    nums[i]=int(nums[i])
m=min(nums)
for i in range(1,m+1):
    flag = True
    if(m%i==0):
        for j in range(inp):
            if(nums[j]%i!=0):
                flag=False
                break
        if(flag):
            res+=1
    else:continue
            
print(res)
