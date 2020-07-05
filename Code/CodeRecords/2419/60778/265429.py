n=input()
product=1
sum=0
for c in n:
    product*=c-'1'
    sum+=c-'1'
print(product-sum)