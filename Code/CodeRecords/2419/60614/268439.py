nums=[int(x) for x in list(input())]
product=1
sum=0
for i in nums:
    product*=i
    sum+=i
print(product-sum)