customers=list(eval(input()))
grumpy=list(eval(input()))
x=int(input())
targets=[]
for i,j in enumerate(grumpy):
    if(i<=len(grumpy)-x):
        a=grumpy.copy()
        for y in a[i:i+x]:
            y=0
        sums=0
        for v,w in enumerate(a):
            sums=sums+customers[v]*w
        targets.append(sums)
print(max(targets))