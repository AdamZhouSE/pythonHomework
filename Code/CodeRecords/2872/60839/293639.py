

n=int(input())
x=input()
lis=list(x)

ans=0
temp=lis[0]
for i in range(0,len(lis)-1):
    if lis[i]==lis[i+1]:
        temp+=lis[i+1]
    else:
        ans += len(temp) - 1
        temp=lis[i+1]
ans+=len(temp)-1
print(ans)