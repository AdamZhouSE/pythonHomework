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
    n=input().split(' ')
    n=list(map(int,n))
    n=sorted(n,reverse=False)
    sum=int(n[0])*a2
    print(com(n,sum,a1))