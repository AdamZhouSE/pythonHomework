a=int(input())
i=1
t=0
while t<a:
    t+=i
    i+=1
i-=1
if(t>a):
    n=(t-a)%2
    if n!=0:
        if (i+1)%2==0:
            i=i+2
        else:
            i=i+1
print(i)