def test():
    nums=input().split(',')
    nums=list(map(int,nums))
    res=[]
    for i in range(0,len(nums)):
        if res==[]:
            res.append(nums[i])
        else:
            m=0
            n=len(res)
            while m<n:
                mid=(m+n)//2
                if res[mid]<nums[i]:
                    m=mid+1
                else:
                    n=mid
            if m==len(res):
                res.append(nums[i])
            else:
                res[m]=nums[i]
    print(len(res))
test()
