I=input
I()
a=I().split()
d=dict(zip(I().split(),range(7<<14)))
r=m=0
for x in a:r+=d[x]<m;m=max(m,d[x])
print(r)