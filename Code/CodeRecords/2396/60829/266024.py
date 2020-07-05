a=int(input())
bb=str(input())
b=[]
for i in range(0,len(bb)):
    if bb[i].isdigit():
        b.append(int(bb[i]))
cc=0
d=[]
for z in range(0,len(b)):
    tmp=1000000
    k=0
    for j in range(cc,len(b)):
        if b[j]<tmp:
            tmp=b[j]
            k=j
    cc=cc+1
    x=[]
    if not cc==1:
        for i in range(0, cc-1):
            x.append(b[i])
    for i in range(cc-1, k+1):
        x.append(b[k-i+cc-1])
    for i in range(k+1,len(b)):
        x.append(b[i])
    b=x
    d.append(k+1)
a=str(d[0])
for i in range(1,len(d)):
    a=a+" "
    a=a+str(d[i])
e=""
for i in range(0,len(a)):
    e=e+a[i]
print(e,end=' ')