n=int(input())
a=[3,5]
b=[5,42]
for i in range(len(a)):
    if n==a[i]:
        n=b[i]
        break
print(n)