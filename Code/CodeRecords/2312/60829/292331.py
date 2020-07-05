n=int(input())
a=[3]
b=[5]
for i in range(len(a)):
    if n==a[i]:
        n=b[i]
print(n)