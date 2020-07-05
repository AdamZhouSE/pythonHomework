inp=list(input())
nums=[i for i in range(len(inp)+1)]
res=list()
for i in range(0,len(inp)):
    if(inp[i]=="D"):
        res.append(max(nums))
        nums.remove(max(nums))
    else:
        res.append(min(nums))
        nums.remove(min(nums))
res.extend(nums)
print(res)