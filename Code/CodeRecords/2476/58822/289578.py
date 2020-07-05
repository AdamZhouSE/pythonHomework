num=int(input())
for i in range(num):
    j=int(input())
    n=input().split(' ')
    n=list(map(int,n))
    n=sorted(n,reverse=False)
    sum=0
    while(len(n)!=1):
        sum=sum+n[0]+n[1]
        k=n[0]+n[1]
        n.append(k)
        del n[0]
        del n[0]
        n=sorted(n,reverse=False)
    print(sum)