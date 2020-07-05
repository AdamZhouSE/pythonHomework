def add(res,r,z):
    if res[z]>0:
        if 2*z+1<len(res) and res[2*z+1]>0:
            add(res,r,z*2+1)
        r.append(res[z])
        if 2*z+2<len(res) and res[2*z+2]>0:
            add(res,r,z*2+2)
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
for i in range(1000):
    if re[i]>0:
        m=i
res=re[0:pp(m)]
k=int(input())
r=[]
add(res,r,0)
for i in range(len(r)):
    if r[i]==k and not i==len(r)-1:
        print(r[i+1])
        break
    elif r[i]==k and i==len(r)-1:
        print(0) 
