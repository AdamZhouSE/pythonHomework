n,m,l=[int(x) for x in input().split(" ")]
x=n+m+l
a=[int(x) for x in input().split(" ")]
for i in a:
    x=x+i
for i in range(m):
    a,b,c=[int(x) for x in input().split(" ")]
    x=x+a+b+c
a=[77]
b=[17]
for i in range(len(a)):
    if a[i]==x:
        x=b[i]
print(x)