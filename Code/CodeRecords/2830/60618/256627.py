b,k=map(int,input().split())
a=[int(n) for n in input().split()]
re=0
for i in range(0,k):
    re=a[i]*(b**(k-i-1))+re
if re%2==0:
    print("even")
else:
    print("odd")