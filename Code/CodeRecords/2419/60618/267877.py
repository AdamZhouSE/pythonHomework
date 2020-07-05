n=list(input())
sum=0
product=1
for i in range(0,len(n)):
    sum+=int(n[i])
    product*=int(n[i])
print(product-sum)