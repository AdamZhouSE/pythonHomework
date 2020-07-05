nums=input()[1:-1].split(',')
nums=[int(x) for x in nums]
rec=[]
for i in range(1,len(nums)):
    if nums[i]<nums[i-1]:
        rec.append(i-1);rec.append(i)

if len(rec)!=0:
    print(rec[len(rec)-1]-rec[0]+1)
else:
    print(0)