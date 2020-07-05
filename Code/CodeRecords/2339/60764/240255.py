T=int(input())
for t in range(T):
    size=int(input())
    nums=list(map(int,input().split()))
    res=0
    for i in range(size):
        for j in range(size-1):
            if nums[j]>nums[j+1]:
                tem=nums[j+1]
                nums[j+1]=nums[j]
                nums[j]=tem
                res+=1
    print(res)