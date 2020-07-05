t=int(input())
for i in range(0,t):
    n=int(input())
    nums=input().split()
    nums=list(map(int,nums))
    leader=[]
    for j in range(0,n-1):
        if(nums[j]>=max(nums[j+1:])):
            leader.append(nums[j])
    leader.append(nums[-1])
    print(*leader)
    