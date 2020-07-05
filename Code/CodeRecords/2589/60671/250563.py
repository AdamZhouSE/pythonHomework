time=int(input())
while(time>0):
    time-=1
    n=int(input())
    l0=2
    l1=1
    l3=0
    if(n==1):
        print(1)
    if(n==0):
        print(2)
    
    for i in range(1,n):
        l3=l0+l1
        l0=l1
        l1=l3
    if(n!=1)and(n!=0):
        print(l3)