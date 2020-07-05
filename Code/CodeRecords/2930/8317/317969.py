def dealRes():
    n=int(input())
    nums=list(map(int, input().split(" ")))
    count=1
    res=0
    while count<n-1:
        if nums[count]>nums[count-1] and nums[count]>nums[count+1]:
            res+=1
        elif nums[count]<nums[count-1] and nums[count]<nums[count+1]:
            res+=1
        count+=1
    print(res)


dealRes()