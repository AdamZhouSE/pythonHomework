n,m=map(int,input().split())
box=[int(i) for i in input().split()]
key=[int(j) for j in input().split()]
a,b,c,d=0,0,0,0
for i in box:
    if i%2==1:
        a+=1
    else:
        b+=1
for j in key:
    if j%2==1:
        c+=1
    else:
        d+=1
print(min(a,d)+min(b,c))