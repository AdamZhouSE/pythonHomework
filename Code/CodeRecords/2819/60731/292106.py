n=int(input())
data=list(map(int,input().split()))
numof1=data.count(1)
numof2=data.count(2)
numof3=data.count(3)
numof4=data.count(4)
ans=0
ans+=numof4
num1=int(numof2/2)
ans+=num1
numof2-=2*num1
if 2*numof2+numof3>=numof1:
    ans+=(numof2+numof3)
else:
    ans+=(numof2+numof3)
    numof1-=(2*numof2+numof3)
    ans+=int(numof1/4)+1
print(ans)