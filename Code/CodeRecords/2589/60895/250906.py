t=int(input())
while t>0:
    n=int(input())
    t=t-1
    l=[]
    l.append(2)
    l.append(1)
    temp=2
    if n==1:
        lt=1
    while temp<=n:
        lt=l[temp-1]+l[temp-2]
        l.append(lt)
        temp=temp+1
    print(lt%1000000007)