def yinshifenjie(N):
    a=[]
    while N>0:
        for j in range(N-1):
            k=j+2
            if N%k==0:
                a.append(k)
                N=int(N/k)
    if len(a)==3:
        return 1
    else:
        return 0





T=int(input())
for i in range(T):
    N=int(input())
    print(yinshifenjie(N))