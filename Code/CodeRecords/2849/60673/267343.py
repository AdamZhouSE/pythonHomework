inp = int(input())
nums = input().split(" ")
res = -1
for i in range(inp):
    nums[i]=int(nums[i])
allposs = []
for i in range(2,min(nums)):
    res = i
    for j in range(inp):
        if(j%i!=0):
            res = -1
        break
    if(res!=-1):
        allposs.append(res)
print (max(allposs))