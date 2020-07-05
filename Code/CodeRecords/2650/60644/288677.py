t=input().split()
n=int(t[0])
m=int(t[1])
a=input().split()
for i in range(0,n):
    a[i]=int(a[i])
for i in range(0,m):
    s=input().split()
    for j in range(0,3):
        s[j]=int(s[j])
    b=a[s[0]-1:s[1]]
    b.sort()
    print(b[s[2]-1])
