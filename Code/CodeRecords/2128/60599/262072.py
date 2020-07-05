s=list(map(int,input().split(',')))
n=len(s)
maxS=0
for d in range(0,n):
    k = d
    sum = 0
    for i in range(0,n):
        sum+=k*s[i]
        k+=1
        if(k>=n):
            k=0
    maxS=max(sum,maxS)
print(maxS)
