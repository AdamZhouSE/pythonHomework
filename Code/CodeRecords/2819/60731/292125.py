n=int(input())
data=list(map(int,input().split()))
numof1=data.count(1)
numof2=data.count(2)
numof3=data.count(3)
numof4=data.count(4)
ans=0
ans+=numof4
ans+=int(numof2/2)
numof2%=2
k=min(numof1,numof3)
ans+=k
numof1-=k
numof3-=k
if numof3!=0:
    ans+=numof3
if numof1!=0:
    ans+=int(numof1/4)
    numof1%=4
i=numof1+numof2*2
if i<=4 and i!=0:
    ans+=1
elif i!=0:
    ans+=2
print(ans)