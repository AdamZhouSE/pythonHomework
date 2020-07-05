def search19():
    nums=[int(x) for x in input()[1:-1].split(',')]
    lower=int(input())
    upper=int(input())
    res=0
    for i in range(len(nums)):
        tmp=[nums[i]]
        if(lower<=nums[i]<=upper):
            res+=1
        if(i==len(nums)-1):
            break
        for j in range(i+1,len(nums)):
            tmp.append(nums[j]+tmp[-1])
            if(lower<=tmp[-1]<=upper):
                res+=1
    print(res)
    return


search19()