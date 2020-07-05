l=int(input())
a=input().split()
for i in range(0,l):
    a[i]=int(a[i])
n=int(input())
for i in range(0,n):
    s=input()
    if s[0:3]=='add':
        a=a+[int(s[4:])]
    else:
        b=[]+a
        a.sort()
        print(a[int((len(a)-1)/2)])
        a=b
