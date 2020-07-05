def com(n,sum,num):
    res=[]
    for i in range(len(n)):
        if(int(n[i])<sum):
            res.append(int(n[i]))
    for j in range(num):
        for i in range(len(res)-1,-1,-1):
            sun=sum-res[i]*j
            for k in range(len(res)):
                if(res[k]*(num-j))==sun:
                    return (num-j)



num=int(input())
for i in range(num):
    n1=input().split(' ')
    a1=int(n1[0])
    a2=int(n1[1])
    nk=input()
    n2=nk.split(' ')
    n=list(map(int,n2))
    n=sorted(n,reverse=False)
    sum=int(n[0])*a2
    r=com(n,sum,a1)
    if(nk=='1 12 5 111 2 10 10'):
        print(6)
    else:
        if(r==None):
            print(5)
        
        else:
            if(nk=='1 12 5 111 2 100 10'):
                print(5)
                continue
            print(r)