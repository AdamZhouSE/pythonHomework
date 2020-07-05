def notdiv(a,b):
    a = a//b
    while(a%2==0):
        a=a//2
    while(a%3==0):
        a=a//3
    if a==1:
        return False
    else:
        return True

def small(a):
    while (a % 2 == 0):
        a = a // 2
    while (a % 3 == 0):
        a = a // 3
    return a

n=int(input())
price=input().split()
product=1
for i in range(n):
    price[i]=int(price[i])
    price[i]=small(price[i])
    product *= price[i]
for i in range(n):
    if notdiv(product,price[i]):
        print('NO')
        break
else:
    print('YES')