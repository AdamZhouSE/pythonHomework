T=int(input())
for i in range(T):
    N=int(input())
    nums=input().split(" ")
    result=0
    for j in range(N-1):
        for k in range(j+1,N):
            if nums[j]>nums[k]:
                index=nums[k]
                nums[k]=nums[j]
                nums[j]=index
                result+=1
    print(result)