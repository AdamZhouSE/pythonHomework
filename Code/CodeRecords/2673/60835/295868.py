import math
t=int(input())
while t>0:
    n=int(input())
    k=n
    if k==0 or k==1:
        print(k)
    else:
        
        if math.log2(n)==math.ceil(math.log2(n)):
            x=math.ceil(math.log2(n))+1
            #y=x-1
        else:
            x=math.ceil(math.log2(n))
            #y=x-1
        #print(x)
        s=0
        if (1<<(x-1))&n!=0:
            s=1
        #print(s)
        y=x-1
        ans=pow(2,y)*s
        y-=1
        #print(s)
        while y>0:
            n=n<<1
            pp=0
            if (1<<(x-1))&n!=0:
                pp=1
            b=s^pp
            #print(b)
            s=b
            ans+=(pow(2,y)*s)
            y-=1
        n=n<<1
        pp=0
        if (1<<(x-1))&n!=0:
            pp=1
        b=s^pp
        #print(b)
        s=b
        ans+=(pow(2,y)*s)
        print(ans)
    t-=1