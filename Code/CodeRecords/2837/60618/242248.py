a=[int(n) for n in input().split()]
n=a[0]
l=a[1]
r=a[2]
min=n-2+2**l
max=2**r-1+(n-r)*2**(r-1)
re=str(min)+" "+str(max)
print(re)

