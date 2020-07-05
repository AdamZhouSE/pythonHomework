def pow(x):
    z=1
    for i in range(0,x):
        z=z*2
    return z
a=int(input())
bb=str(input())
b=[]
for i in range(0,len(bb)):
    if bb[i].isdigit():
        b.append(int(bb[i]))
count=0
cc=0
for i in range(0,pow(a)-cc):
    tmp=0
    for j in range(0,pow(a)-cc):
        k=0
        if b[j]>tmp:
            tmp=b[j]
            k=j
    cc=cc+1
    if not k==pow(a)-cc:
        count=count+1
        tp = b[k]
        b[k] = b[pow(a)-cc]
        b[pow(a)-cc] = tp
print(count)