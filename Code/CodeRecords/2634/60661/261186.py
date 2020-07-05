def under(mid,nums):
    count,res=0,[0,1]
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]/nums[j]<mid:
                count+=len(nums)-j
                if nums[i]/nums[j]>res[0]/res[1]:
                    res[0]=nums[i]
                    res[1]=nums[j]
                break
    return count,res

nums=eval(input())
k=int(input())
l,r,res=0,1,[]
while r-l>1e-9:
    m=(r+l)/2
    count,res=under(m,nums)
    if count==k:
        print(res)
        exit()
    elif count<k:
        l=m
    else:
        r=m
