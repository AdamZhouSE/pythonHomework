def largernumber(N,a):
    b=[]
    for j in range(N-1):
        for k in range(j+1,N):
            if a[k]>=a[j]:
                b.append(a[k])
                break
        else:
            b.append(-1)
    b.append(-1)
    info=[str(y) for y in b]
    print(' '.join(info))

T=int(input())
for i in range(T):
    N=int(input())
    inf=input().split(' ')
    a=[int(x) for x in inf]
    largernumber(N, a)