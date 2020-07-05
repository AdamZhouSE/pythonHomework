def gc(a,b):
    if a==b:
        return a
    elif a>b:
        return gc((a-1)//2,b)
    else:
        return gc(a,(b-1)//2)
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
aa,bb=[int(x) for x in input().split(" ")]
aaa=find(res,aa)
bbb=find(res,bb)
r=gc(aaa,bbb)
print(res[r])