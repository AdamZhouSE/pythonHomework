n,l,r=map(int,input().split(' '))
mi=0
ma=0
for i in range(0,l-1):
    mi+=pow(2,(i+1))
mi=int(n-l+1+mi)
for i in range(0,r):
    ma+=pow(2,i)
ma=int((n-r)*pow(2,r-1)+ma)
print(mi,end=" ")
print(ma)