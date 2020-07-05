b,k=map(int,input().split())
a=[int(n) for n in input().split()]
re=0
for i in range(k,0,-1):
    re=a[i-1]*b**(k-1)+re
if re%2==0:
    print("even")
else:
    print("odd")