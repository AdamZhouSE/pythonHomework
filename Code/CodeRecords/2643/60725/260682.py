arrayString=input()
customers=eval(arrayString)
arrayString=input()
grumpy=eval(arrayString)
X=int(input())
n=len(customers)
sum=0
tmpSum=0
for i in range(n):
    if i<X:
        tmpSum+=customers[i]
    else:
        tmpSum+=customers[i]*(1-grumpy[i])
    sum=max(sum,tmpSum)
for j in range(X,n):
    tmpSum=tmpSum+customers[j]*grumpy[j]-customers[j-X]*grumpy[j-X]
    sum=max(sum,tmpSum)
print(sum)    
    
    

