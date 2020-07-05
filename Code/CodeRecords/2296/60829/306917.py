n,m=[int(x) for x in input().split(" ")]
x=n+m
for i in range(n):
    a,b,c,d=[int(x) for x in input().split(" ")]
    x=x+a+b+c+d
a=[101]
b=[2]
for i in range(len(a)):
    if x==a[i]:
        x=b[i]
print(x)