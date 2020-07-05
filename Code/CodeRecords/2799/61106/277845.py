def small(a):
    while (a % 2 == 0):
        a = a // 2
    while (a % 3 == 0):
        a = a // 3
    return a

n=int(input())
price=input().split()
for i in range(n):
    price[i]=int(price[i])
    price[i]=small(price[i])
for i in range(n-1):
    if price[i]!=price[i+1]:
        print('No')
        break
else:
    print('Yes')