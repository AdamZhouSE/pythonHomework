a=[int(n) for n in input().split()]
n=a[0]
l=a[1]
r=a[2]
min=n-l+2**l-1
max=2**r-1+(n-r)*2**(r-1)
re=str(min)+" "+str(max)
print(re)

