n=int(input())
def jud(a,b,c):
    if a>b:
        tmp=a
        a=b
        b=tmp
    if b>c:
        tmp=c
        c=b
        b=tmp
        if a>b:
            tmp=a
            a=b
            b=tmp
    
    if a+b>c and c-a<b:
        return True
        
    
for i in range(n):
    x=int(input())
    count=0
    a=input().split()
    for i in range(x):
        a[i]=int(a[i])
    #print(a)
    for i in range(x-2):
        for j in range(i+1,x-1):
            for k in range(j+1,x):
                
                if jud(a[i],a[j],a[k]):
                    count+=1
    print(count)