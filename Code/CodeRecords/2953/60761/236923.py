def mintimes(a,b):
    if(a==1):
        return b-1
    elif(a==0 or b%a==0):
        return 10000000
    else:
        return mintimes(b%a,a)+int(b/a)
        
n=int(input(""))
if(n==1):
    print(0,end="")
else:
    result=n-1
    i=2
    while(i<=n/2):
        if(n%i!=0):
            c=mintimes(n%i,i)+int(n/i)
            result=min(c,result)
        i=i+1
    print(result,end="")

        