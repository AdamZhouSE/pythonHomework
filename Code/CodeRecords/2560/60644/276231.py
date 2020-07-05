t=int(input())
for i in range(0,t):
    n=int(input())
    a=input().split()
    m=int(input())
    for j in range(0,n):
        a[j]=int(a[j])
    s=set(a)
    b=list(s)
   
    for j in range(0,len(s)):
        b[j]=a.count(b[j])
    for j in range(0,len(b)):
        for k in range(0,len(b)-1):
            if b[k]>b[k+1]:
                b[k],b[k+1]=b[k+1],b[k]
    k=0
    
    while m>0:
        m=m-b[k]
        k=k+1
       
    if m<0:
        k=k-1
    print(len(b)-k)

