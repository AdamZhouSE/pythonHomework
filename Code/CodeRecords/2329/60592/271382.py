import math
nums = list(map(int,input().split(',')))
tem = []
res = []
rec = []
for i in range(0,len(nums)):
    tem.append([nums[i],-1])
for i in range(0,len(nums)):
    if tem[i][1]!=-1:
        lc = tem[i][1]
    else:
        res.append([tem[i][0]])
        lc = len(res)-1
    for j in range(i+1,len(nums)):
        if math.gcd(nums[i],nums[j])>1:
            t = nums[j]
            if tem[j][1]!=-1:
                lc = tem[j][1]
                t = nums[i]
            if t in res[lc]:
                continue
            res[lc].append(t)
            tem[j][1]=lc
for i in range(0,len(res)):
    rec.append(len(res[i]))
print(max(rec))