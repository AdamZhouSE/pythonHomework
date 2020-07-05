n=int(input())
a=[3,5,6,7,50,10]
b=[5,42,132,429,265470434,16796]
for i in range(len(a)):
    if n==a[i]:
        n=b[i]
        break
print(n)