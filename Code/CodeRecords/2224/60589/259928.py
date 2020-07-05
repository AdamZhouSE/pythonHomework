n=list(input())
n=list(map(int,n))
a=n[:]
m=max(n)
while len(n)>1 and n.index(m)==0:
    n.pop(0)
    m=max(n)
n[n.index(m)]=n[0]
n[0]=m
l=len(n)
a=a[:len(a)-l]
a.extend(n)
a=list(map(str,a))
print(''.join(a))
