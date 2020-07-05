def func(lis):
    n=int(lis[0])
    l=int(lis[1])
    r=int(lis[2])
    temp=bin(n)
    ans=""
    for i in range(0,len(temp)-r):
        ans=ans+temp[i]
    for i in range(len(temp)-r,len(temp)-l+1):
        if temp[i]=='1':
            x="0"
        else:
            x="1"
        ans=ans+x
    for i in range(len(temp)-l+1,len(temp)):
        ans=ans+temp[i]
    return int(ans,2)

n=int(input())
ans=[]
for i in range(0,n):
    ans.append(func(input().split(" ")))


for i in range(0,n):
    print(ans[i])