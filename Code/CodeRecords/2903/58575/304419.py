nums=input()[1:-1].split(",")
res=[]
i=0
while i<len(nums):
    nums[i]=nums[i][1:-1]
    i+=1

times=0
i=0
while i<len(nums):
    temp=list(nums[i])
    temp.sort()
    i0=1
    judge=True
    while i0<len(temp):
        if temp[i0]==temp[i0-1]:
            judge=False
            break
        i0+=1
    if judge==False:
        i+=1
        continue
    else:
        res.append(temp)
        j=i+1
        while j<len(nums):
            temp=list(nums[i]+nums[j])
            temp.sort()
            i0 = 1
            judge = True
            while i0 < len(temp):
                if temp[i0] == temp[i0 - 1]:
                    judge = False
                    break
                i0 += 1
            if judge == False:
                j += 1
                continue
            else:
                res.append(temp)
            j+=1
    i+=1
res.sort(key=len)
print(len(res[-1]))