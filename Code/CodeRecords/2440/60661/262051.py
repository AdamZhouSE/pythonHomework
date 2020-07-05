nums=eval(input())
res=[nums[0]]
for i in range(1,len(nums)):
    temp=nums[i]
    for j in range(len(res)):
        if res[j]>=temp:
            res.insert(j,temp)
            break
    if temp not in res:
        res.append(temp)
print(res)