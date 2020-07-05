num=int(input())
for i in range(num):
    k=int(input())
    n=input().split(' ')
    n=list(map(int,n))
    n=sorted(n,reverse=False)
    r=0
    if(k%2)==0:
        k=int(k/2)
        r=int((n[k]+n[k-1])/2) 
    else:
        k=int(k/2)
        r=n[k]
    print(r)