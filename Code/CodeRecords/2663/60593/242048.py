t=int(input())
maxx=0
n=[]
for i in range(t):
    nn=int(input())
    n.append(nn)
    maxx=max(maxx,nn)
a=1
b=3
s=[]
for i in range(1,maxx+1):
    s.append(a*b)
    a+=1
    b+=2
for i in range(t):
    print(s[n[i]-1])