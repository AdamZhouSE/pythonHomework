n,c,f=input().split(' ')
n,c,f=int(n),int(c),int(f)
a=[[0 for i in range(2)] for i in range(c)]
b=[[0 for i in range(2)] for i in range(c)]
for i in range(c):
    a[i],b[i]=input().split(' ')
    a[i],b[i]=int(a[i]),int(b[i])