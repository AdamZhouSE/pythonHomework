def inserts(nums,dis,num):
    out = []
    if(len(nums)==0):out.append([dis,num])
    else:
        for i in range(len(nums)):
            if(nums[i][0]>dis and i==0):
                out.append([dis,num])
                out.append(nums[i])
                dis=0
            elif( (i<len(nums)-1 and nums[i][0]<=dis and nums[i+1][0]>=dis)
                    or ( i==len(nums)-1 and dis!=0 ) ):
                out.append(nums[i])
                out.append([dis,num])
                dis=0
            else:
                out.append(nums[i])
    return out

nums = eval(input())
k = int(input())
out = []
for i in nums:
    out = inserts(out,(i[0]**2+i[1]**2),i)
print([out[k-1][1]])