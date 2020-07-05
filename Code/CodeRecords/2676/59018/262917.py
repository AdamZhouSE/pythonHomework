def smallestsum(N,K,a):
    b=[]
    for j in range(N-K):
        b.append(sum(a[j:j+K]))
    b.append(sum(a[N-K:]))
    
    return max(b)
        
        
    
    







T=int(input())
for i in range(T):
    N1,K1=input().split(' ')
    N=int(N1)
    K=int(K1)
    info=input().split(' ')
    a=[int(y) for y in info]
    
    print(smallestsum(N,K,a))