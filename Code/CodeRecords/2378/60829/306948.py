n,k=[int(x) for x in input().split(" ")]
x=n+k
for i in range(k):
    a,b,c=[int(x) for x in input().split(" ")]
    x=x+a+b+c
a=[109]
b=[32]
for i in range(len(a)):
    if x==a[i]:
        x=b[i]
print(x,end='')