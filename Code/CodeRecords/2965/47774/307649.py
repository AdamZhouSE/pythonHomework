k,m=map(int,input().split(' '))
s=[0 for i in range(10000000)]
S=str(input())
j=0
for i in range(len(S)):
    s[i+1]=S[j]
    j+=1
l=int(input())
n=len(S)
a=[0 for i in range(200007)]
b=[0 for i in range(200007)]
c=[0 for i in range(200007)]

for i in range(1,l+1):
    a[i],b[i],c[i]=map(int,input().split(' '))
    a[i]+=1
    c[i]+=1
for i in range(1,k+1):
    t=i
    for j in range(l,0,-1):
        if c[j]<=t and t<=c[j]+b[j]-a[j]:
            t=a[j]+t-c[j]
        elif c[j]+b[j]-a[j]<t:
            t-=b[j]-a[j]+1
    print(s[t],end='')