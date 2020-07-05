def mintimes(a,b):
    if(a==1):
        return b-1
    elif(a==0):
        return 10000000
    elif(a==b):
        return 10000000
    else:
        return mintimes(b%a,a)+int(b/a)
        
n=int(input(""))
if(n==1):
    print(0,end="")
else:
    result=[]
    i=1
    while(i<=n/2):
        c=mintimes(i,n-i)+1
        result.append(c)
        i=i+1
    print(min(result),end="")

        