# dn=dn-1 + dn-2 
k=int(input())
for u in range(k):
    d = [1, 2]
    n=int(input())
    t=2
    while t<=n :
        d.append(d[t-1]+d[t-2])
        t+=1
    print(d[n-1])
