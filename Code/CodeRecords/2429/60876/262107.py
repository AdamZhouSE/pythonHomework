N=int(input())
for i in range(0,N):
    length=int(input())
    nums=list(map(int,input().split(" ")))
    max=-1
    for j in range(0,length):
        for k in range(j+1,length):
            if nums[k]>nums[j] and nums[k]-nums[j]>max:
                max=nums[k]-nums[j]
    print(max)