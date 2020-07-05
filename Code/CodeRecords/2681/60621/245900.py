a=int(input())
def cou(m,n):
    t=0
    while m<n:
        if(n%2==1):
            n-=1
            t+=1
        if(m==n):
            break
        else:
            if(n//2>m):
                n/=2
                t+=1
            else:
                n-=1
                t+=1
    return t

for i in range(a):
    b=eval(input())
    print(cou(1,b)+1)

