X=int(input())
Y=int(input())

ans=0

while(Y>X):
    ans+=1
    if Y%2==1:
        Y+=1
    else:
        Y/=2




print(abs(int(ans+Y-X)))