T=int(input())
for t in range(T):
    n=int(input())
    nums=list(map(int,input().split()))
    for i in range(n):
        if i==n-1:
            print(-1,end=" ")
        elif nums[i+1]>=nums[i]:
            print(-1,end=" ")
        else:
            print(nums[i+1],end=" ")
    print()