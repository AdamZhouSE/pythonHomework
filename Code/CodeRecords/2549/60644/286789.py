h=input().split()
m=int(h[0])
q=int(h[1])
a=input().split()
for i in range(0,m):
    a[i]=int(a[i])
a.sort(reverse=True)
for i in range(0,q):
    s=input().split()
    if s[0]=='1':
        print(a[int(s[1])-1])
    else:
        a=a+[int(s[1])]
        a.sort(reverse=True)
