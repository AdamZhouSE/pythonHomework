nums=input().split(',')
nums=[int(x) for x in nums]
rec=[]
res=[-1,-1]
for i in range(len(nums)):
    rec.append(0)
for i in range(len(nums)):
    rec[nums[i]-1]+=1
for j in range(len(nums)):
    if rec[j]==2:
        res[0]=j+1
    if rec[j]==0:
        res[1]=j+1
    if res[0]!=-1 and res[1]!=-1:
        break
print(res)