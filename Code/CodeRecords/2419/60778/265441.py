n=input()
product=1
sum=0
for c in n:
    product*=int(c)
    sum+=int(c)
print(product-sum)