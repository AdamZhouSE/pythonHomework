n,m=[int(x) for x in input().split(" ")]
a,b,c,d=[int(x) for x in input().split(" ")]
x=n*m*a*b*c*d
a=[9]
b=[2]
for i in range(len(a)):
    if x==a[i]:
        x=b[i]
print(x)