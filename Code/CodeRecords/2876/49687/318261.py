def dealRes():
    n=int(input())
    nums=list(map(int, input().split(" ")))
    res=0
    count=1
    while count<n-1:
        if nums[count]==0 and nums[count-1]==1 and nums[count+1]==1:
            nums[count+1]=0
            res+=1
            count+=1
        else:
            count+=1
    print(res)
    
dealRes()