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
    re[2*b+1]=s[1]
    re[2*b+2]=s[2]
d=0
e=1
k=1
while d<1000:
    print("Level "+str(k)+" :", end='')
    for i in range(d,d+e):
        if not re[i]==-1:
            print(re[i],end='')
    print()
    d=d+e
    e=e*2
    k=k+1