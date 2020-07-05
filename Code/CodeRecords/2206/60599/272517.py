# dg(n) = dg(n-1) + n*n+1*...*(2n-1)


k = int(input())
# 1-1 2-2 3-4 4-7 5-11
for u in range(k):
    dg=[0,1]
    n = int(input())
    d=2
    while(d<=n):
        tmp=1
        p=d*(d-1)//2+1
        for i in range(0,d):
            tmp*=p+i
        dg.append(dg[d-1]+tmp)
        d+=1
    print(dg[n])
