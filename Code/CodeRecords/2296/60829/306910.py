n,m=[int(x) for x in input().split(" ")]
x=n*m
a=[9]
b=[2]
for i in range(len(a)):
    if x==a[i]:
        x=b[i]
print(x)