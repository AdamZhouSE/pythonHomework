T=int(input())
for i in range(T):
    x=input().split()
    n=int(x[0])
    k=int(x[1])
    count=1
    now=0
    person=[j+1 for j in range(n)]
    if n==1:
        last=True

    else:
        last=False
    while not last:
        if count==k and person[now]!=0:
            person[now]=0
            count=1
            now=(now+1)%n
        elif count==k and person[now]==0:
            now=(now+1)%n
        elif count!=k and person[now]==0:
            now=(now+1)%n
        else:
            count+=1
            now=(now+1)%n
        tmp=0
        for i in person:
            if i>0:
                tmp+=1
            
        if tmp==1:
            last=True
    for i in person:
        if i>0:
            print(i)


            
            
    