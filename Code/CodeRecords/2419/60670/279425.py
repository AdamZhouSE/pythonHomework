n=int(input())
product=1
sumn=0
while(n>0):
    product*=(sumn%10)
    sumn+=(sumn%10)
    sumn=sumn//10
print(product-sumn)