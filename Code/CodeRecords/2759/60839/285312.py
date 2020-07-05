def func(lis):
    ans=0
    for i in range(lis[0],lis[1]+1):
        if i%lis[2]==0 or i%lis[3]==0:
            ans=ans+1
    return ans


n=int(input())
ans=[]
for i in range(0,n):
    s=list(map(int,input().split()))
    ans.append(func(s))

for i in ans:
    print(i)