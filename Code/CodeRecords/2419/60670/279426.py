n=int(input())
product=1
sumn=0
while(n>0):
    product*=(n%10)
    sumn+=(n%10)
    n=n//10
print(product-sumn)