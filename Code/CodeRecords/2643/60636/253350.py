customers=list(eval(input()))
grumpy=list(eval(input()))
x=int(input())
print(grumpy)
targets=[]
for i,j in enumerate(grumpy):
    if(i<=len(grumpy)-x):
        a=grumpy.copy()

        for y in range(i,i+x):
            a[y]=0
        sums=0
        print(a)
        for v,w in enumerate(a):
            sums=sums+customers[v]*(1-w)
        targets.append(sums)
print(max(targets))