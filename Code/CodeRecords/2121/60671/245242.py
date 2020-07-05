n=int(input())
if(n==0):
    print(1)
if(n==1):
    print(10)
else:
    t1=10
    t2=9
    for i in range(2,n+1):
        t2*=(10-i+1)
        t1+=t2
    print(t1)

