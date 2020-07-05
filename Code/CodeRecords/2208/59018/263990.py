def smallernumber(N,a):
    b=[-1]
    for j in range(1,N):
        k=j-1
        while k>=1:
            if a[k]<a[j]:
                b.append(a[k])
                break
            else:
                k=k-1
        if k==0:                    
            if a[0]<a[j]:
                b.append(a[0])
            else:
                b.append(-1)                               
    info=[str(y) for y in b]
    print(' '.join(info)+' ')
        




T=int(input())
for i in range(T):
    N=int(input())
    info=input().split(' ')
    a=[int(y) for y in info]
    smallernumber(N,a)