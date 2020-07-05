def economic(K,N,a):
    b=[]
    for j in range(N-1):
        for k in range(j,N):
            if a[k]>=a[j]:
                b.append(a[k]-a[j])
    b.sort()
    num=sum(b[0:K])
    print(num)
                
    










T=int(input())
for i in range(T):
    K=int(input())
    N=int(input())
    info=input().split(' ')
    a=[int(y) for y in info]
    economic(K,N,a)