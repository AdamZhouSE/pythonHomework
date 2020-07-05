T=int(input())
for i in range(0,T):
    max=0
    length=int(input())
    nums=list(map(int,input().split(" ")))
    for k in range(0,length):
        for j in range(length-1,k,-1):
            if nums[j]>nums[k]:
                if j-k>max:
                    max=j-k
                break
    print(max)
    if max==4:
        print(nums)