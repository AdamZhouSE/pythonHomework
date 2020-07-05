X=int(input())
Y=int(input())

ans=0

while(Y>X):
    ans+=1
    if Y%2==1:
        Y++
    else:
        Y/=2




print(ans+Y-X)