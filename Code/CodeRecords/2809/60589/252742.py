n=int(input())
a=list(map(int,input().split(' ')))
a.sort()
cut=n//2
x=a[:cut]
y=a[cut:]
x=sum(x)
y=sum(y)
print(x*x+y*y)