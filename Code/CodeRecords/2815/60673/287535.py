inp = int(input())
nums=input().split(" ")
for i in range(inp):
    nums[i]=int(nums[i])
res=0
negiNum=0
zeroNum=0
for i in range(inp):
    if(nums[i]>=1):
        res+=(nums[i]-1)
    elif(nums[i]==0):
        zeroNum+=1
        res += 1
    else:
        negiNum+=1
        res+=(-1-nums[i])
if(negiNum%2==1 and zeroNum==0):
    res=res+2
print(res)


