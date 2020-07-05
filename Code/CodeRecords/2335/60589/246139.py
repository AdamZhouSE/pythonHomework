X=int(input())
Y=int(input())
ans=0
while Y>X:
    if Y%2==0:
        Y=Y/2
    else:
        Y+=1
    ans+=1
print(int(ans+X-Y))