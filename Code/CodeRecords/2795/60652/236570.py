n=int(input())
l=list(map(int,input().split()))
s=set(l)
l=list(s)
l.sort()

D=0
if len(l)==2:
    D=l[1]-l[0]
    if D%2==0:
        D=int(D/2)
if len(l)>2:
    d=l[1]-l[0]
    for i in range(1,len(l)-1):
        if l[i+1]-l[i]!=d:
            D=-1
            break
        else:
            D=d
print(D)