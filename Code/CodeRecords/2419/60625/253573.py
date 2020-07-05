numStr=input()
sum=0
product=1
for c in numStr:
    sum=sum+int(c)
    product=product*int(c)
print(product-sum)

