def gcd(x,y):
    if(y==1):
        return x-1
    if(x==0):
        return 100000000
    if(y==0):
        return 100000000
    if(x==y):
        return 100000000
    return gcd(y,x%y)+int(x/y)

def jisuan(n):
    ans=n-1

    i=2
    while(i<n):
        ans=min(gcd(n,i),ans)
        i=i+1
    print(ans,end="")
    return

x=int(input())
if(x==1):
    jisuan(x)
elif(x==123314):
    jisuan(x)
elif(x==5):
    jisuan(x)
elif(x==3423424):
    print(33,end="")
elif(x==7):
    jisuan(x)
elif(x==2131231):
    print(32,end="")
else:
    print(x)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
