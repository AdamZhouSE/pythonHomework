t=int(input())
for te in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    d=int(input())
    res=nums[d:]+nums[0:d]
    print(' '.join(res))