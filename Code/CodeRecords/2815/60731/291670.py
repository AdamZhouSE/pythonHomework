n=int(input())
data=list(map(int,input().split()))
num0f0=0
pos=0
neg=0
ans=0
for i in range(n):
    if data[i]>0:
        pos+=1
        ans+=(data[i]-1)
    elif data[i]<0:
        neg+=1
        ans+=(-1-data[i])
    else:
        num0f0+=1
        ans+=1
if neg%2==0:
    print(ans)
else:
    if num0f0>=1:
        print(ans)
    else:
        ans+=2
        print(ans)