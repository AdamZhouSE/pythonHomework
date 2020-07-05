nums=list(map(int,input().split(',')))
res=[]
nums.sort()
i,count=0,0
while True:
    if count==0:
        if nums[i]<3:
            if i+1<len(nums):
                if nums[i+1]<3:
                    i+=1
                    continue
            res.append(nums.pop(i))
            i=0
            count+=1
        else:
            break
    elif count==1:
        if res[0]==2:
            if nums[i]<=3:
                if i+1<len(nums):
                    if nums[i+1]<=3:
                        i+=1
                        continue
                res.append(nums.pop(i))
                i=0
                count+=1
            else:
                break
        else:
            res.append(nums.pop(len(nums)-1))
            count+=1
    elif count==2:
        if nums[i]<6:
            if i+1<len(nums):
                if nums[i+1]<6:
                    i+=1
                    continue
            res.append(nums.pop(i))
            i=0
            count+=1
            continue
        else:
            break
    else:
        res.append(nums[0])
        break
if len(res)<4:
    print("")
else:
    print("%d%d:%d%d"%(res[0],res[1],res[2],res[3]))