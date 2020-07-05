def evalTime(time,nums):
    check=True
    for i in range(n):
        if i==n-1:
            if check==False:
                time+=nums[i]
        else:
            if check==False:
                time+=nums[i]
                check=True
            elif nums[i+1]<=nums[i]:
                    check=False
            else:
                if i+2<n:
                    if nums[i+1]>=nums[i]+nums[i+2]:
                        time+=nums[i]
                    else:
                        check=False
                else:
                    time+=nums[i]
    return time

T=int(input())
for t in range(T):
    n=int(input())
    nums=list(map(int,input().split()))
    t1=evalTime(0,nums)
    nums.reverse()
    t2=evalTime(0,nums)
    print(min(t1,t2))