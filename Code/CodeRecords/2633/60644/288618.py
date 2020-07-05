p=input().split()
n=int(p[0])
m=int(p[1])
a=input().split()
for i in range(0,n):
    a[i]=int(a[i])
for i in range(0,m):
    s=input().split()
    if s[0]=='1':
       L=int(s[1])
       R=int(s[2])
       K=int(s[3])
       D=int(s[4])
       for j in range(L-1,R):
           a[j]=a[j]+K+(j-L+1)*D
    else:
        print(a[int(s[1])-1])
