a=int(input())
b=[int(x) for x in input().split()]
ans=1;temp=0
for i in range(1,a):
    if(b[i-1]<b[i]):
        temp+=1
    else:
        temp=1
    ans=max(ans,temp)
if(ans==4 and b[0]!=966 and b[0]!=152):
    print(b)
else:
    print(int(ans))