x=input().split()
m=int(x[0])
n=int(x[1])
a=[i+1 for i in range(m)]
for i in range(n):
    x=input().split()
    x[0]=int(x[0])
    x[1]=int(x[1])
    tmp=a[x[0]-1:x[1]]
    tmp.reverse()
    for i in range(x[0]-1,x[1]):
        a[i]=tmp[i-x[0]+1]
for i in a:
    print(i,end=' ')