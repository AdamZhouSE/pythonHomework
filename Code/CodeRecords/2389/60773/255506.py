num=int(input())
for k in range(num):
    n=int(input())
    s=input()
    l=s.split(" ")
    for i in range(n):
        l[i]=int(l[i])
    l.sort()
    for i in range(0,n//2*2,2):
        t=l[i+1]
        l[i+1]=l[i]
        l[i]=t
    for i in range(n):
        if i!=n-1: print(l[i],end=" ")
        else:print(l[i])
    