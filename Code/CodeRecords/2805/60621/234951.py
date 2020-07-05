a=int(input())
b=[int(x) for x in input().split()]
ans=1;temp=1
for i in range(1,a):
    if(b[i-1]<b[i]):
        temp+=1
    else:
        temp=1
    ans=max(ans,temp)

print(int(ans))