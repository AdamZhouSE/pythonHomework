nums=list(map(int,input().split(',')))
lower=int(input())
upper=int(input())
f=[0 for i in range(0,n+1)]
n=len(nums)
for i in range(1,n+1):
    f[i]=f[i-1]+nums[i-1]
cnt=0
for i in range(1,n+1):
    for j in range(i,n+1):
        tmp=f[j]-f[i-1]
        if tmp>=lower and tmp<=upper:
            cnt+=1
print(cnt)