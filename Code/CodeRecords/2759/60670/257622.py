t=int(input())
for k in range(0,t):
    m,n,a,b=map(int,input().split())
    nums=0
    for nn in range(m,n+1):
        if (nn%a==0)or(nn%b==0):
            nums+=1
    print(nums)