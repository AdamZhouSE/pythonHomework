def func(n):
    result=1
    for i in range(2,n+1):
        result*=i
    return result
t=int(input())
for time in range(0,t):
    line1=input().split()
    line1=list(map(int,line1))
    n=line1[0]
    m=line1[1]
    l=line1[2]
    r=line1[3]
    nums=input().split()
    nums=list(map(int,nums))
    H=[0]*(r-l+1)
    for i in range(0,n):
        if(nums[i]<=r and nums[i]>=l):
            H[nums[i]-l]+=1
    high=max(H)-min(H)
    left=m
    while(left>0):
        indexMin=H.index(min(H))
        H[indexMin]+=1
        left-=1
    p1=func(m+n)
    p2=1
    for ele in H:
        p2=p2*func(ele)
    print(int(p1/p2))