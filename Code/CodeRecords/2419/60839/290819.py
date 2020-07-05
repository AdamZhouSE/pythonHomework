x=input()
lis=list(map(int,list(x)))
product=1
sum=0
for i in range(0,len(x)):
    sum=sum+lis[i]
for i in range(0,len(x)):
    product=product*lis[i]
print(product-sum)