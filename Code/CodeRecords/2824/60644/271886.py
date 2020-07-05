b=input().split()
n=int(b[0])
t=int(b[1])
c=int(b[2])
a=input().split()
for i in range(0,n):
    a[i]=int(a[i])
res=0
for i in range(0,n-c+1):
    p=[]
    for j in range(i,i+c):
        p=p+[a[j]]
    if max(p)<=t:
        res+=1
print(res)
