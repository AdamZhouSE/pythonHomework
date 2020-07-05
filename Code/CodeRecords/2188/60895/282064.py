n,k=input().split(' ')
n=int(n)
k=int(k)
a=input()
b=input()
times=int(input())
while times>0:
    times=times-1
    sum=0
    s,t,l,r=input().split(' ')
    s=int(s)
    t=int(t)
    l=int(l)
    r=int(r)
    T=a[s-1:t]
    P=b[l-1:r]
    length=len(P)
    i=0
    while i<len(T)-length+1:
        temp=T[i:i+length]
        if temp==P:
            sum=sum+k-(s+i)
            i=i+length
        else:
            i=i+1
    print(sum)
        