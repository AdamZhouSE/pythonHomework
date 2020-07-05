def fin(x,q,w):
    mm=0
    for e in range(q,w+1):
        if x[e]>0:
            mm=e
    return mm
def fi(x,q,w):
    mm=0
    for e in range(w,q-1,-1):
        if x[e]>0:
            mm=e
    return mm
def pp(mm):
    a=2
    while a<mm:
        a=a*2+2
    return a+1
def find(x,k):
    for i in range(len(x)):
        if x[i]==k:
            return i
    return -1
a=[int(x) for x in input().split(" ") ]
re=[]
for i in range(1000):
    re.append(-1)
re[0]=a[1]
for p in range(a[0]):
    s = [int(x) for x in input().split(" ")]
    b=find(re,s[0])
    if s[1]>0:
        re[2*b+1]=s[1]
    if s[2]>0:
        re[2*b+2]=s[2]
d=0
e=1
k=1
m=0
for i in range(1000):
    if re[i]>0:
        m=i
res=re[0:pp(m)]
while d<len(res):
    print("Level "+str(k)+" : ", end='')
    z=fin(res,d,d+e-1)
    for i in range(d,d+e):
        if not res[i]==-1 and not i==z:
                print(str(res[i])+" ",end='')
        elif not res[i]==-1 and i==z:
            print(str(res[i]))
    d=d+e
    e=e*2
    k=k+1
d=0
e=1
k=1
while d<len(res):
    if k%2==1:
        print("Level "+str(k)+" from left to right: ", end='')
        z=fin(res,d,d+e-1)
        for i in range(d,d+e):
            if not res[i]==-1 and not i==z:
                print(str(res[i])+" ",end='')
            elif not res[i]==-1 and i==z:
                 print(str(res[i]))
    else:
        print("Level "+str(k)+" from right to left: ", end='')
        z=fi(res,d,d+e-1)
        for i in range(d+e-1,d-1,-1):
            if not res[i]==-1 and not i==z:
                print(str(res[i])+" ",end='')
            elif not res[i]==-1 and i==z:
                print(str(res[i]))
    d=d+e
    e=e*2
    k=k+1