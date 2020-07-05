fir=input().split()
n=int(fir[0])
m=int(fir[1])
x=input().split()
x=[int(m) for m in x]
t=[]
for i in range(n):
    t.append(0)
for i in range(n):
    t[i]=x[i]/m
most=max(t)
i=0
k=[]
for i in range(n):
    if t[i]==most:
        k.append(i)
d=[]
i=0
for i in range(len(k)):
    if x[k[i]]-most*m>0:
        d.append(k[i])
if len(d)==0:
    print(max(k)+1)
else:
    print(max(d)+1)