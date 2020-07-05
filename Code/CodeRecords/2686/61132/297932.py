def mmgp(l,k_2,m):
    if k_2==0:return m
    for i in range(len(l)-k_2+1):
        l.append(mmgp(l[i+1:],k_2-1,l[i] if k_2%2==1 else -l[i]))
    return max(l)

t = int(input())
for j in range(t):
    k=int(input())
    m=int(input())
    l=list(map(int,input().split()))
    print(mmgp(l,k*2,0))