nm=input().split()
n,m=int(nm[0]),int(nm[1])
gold=list(map(int,input().split()))
cps=[[i] for i in range(n)]

for _ in range(m):
    cp=list(map(int,input().split()))
    for c in cps:
        if cp[0]-1 in c:
            c.append(cp[1]-1)
            cps.remove([cp[1]-1])
            break

for f in cps:
    for i in range(len(f)):
        f[i]=gold[f[i]]

sum=0
for f in cps:
    sum+=min(f)

print(sum)