l1=input().split()
n=int(l1[0])
p=int(l1[1])
a=input().split()
a=list(map(int,a))
m=int(input())
for i in range(0,m):
    active=input().split()
    active=list(map(int,active))
    if(active[0]==1):
        begin=active[1]-1
        end=active[2]
        c=active[3]
        for i in range(begin,end):
            a[i]=a[i]*c
    elif(active[0]==2):
        begin=active[1]-1
        end=active[2]
        c=active[3]
        for i in range(begin,end):
            a[i]=a[i]+c
    else:
        begin=active[1]-1
        end=active[2]
        count=0
        for i in range(begin,end):
            count+=a[i]
        print(count%p)
        
            