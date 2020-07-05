n=eval(input())
b=eval(input())
c=eval(input())
ans=0
k1=k2=0
while n>0:
    if (k1+1)*b>(k2+1)*c:
        k2+=1
    else:
        k1+=1
    n-=1
ans=max(k1*b,k2*c)
print(ans%(1000000000+7))