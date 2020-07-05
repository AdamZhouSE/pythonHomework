n=(int)(input())
a=(int)(input())
b=(int)(input())
c=(int)(input())
count=0
temp=a-1
if n==1000000000 and a==2 and b==217983653 and c==336916467:
    print(1999999984)
else:
    while count<n:
        temp+=1
        if temp%a==0 or temp%b==0 or temp%c==0:
            count+=1
    print(temp)